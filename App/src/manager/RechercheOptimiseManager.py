from datetime import datetime, date

from src.database import Mysql
from src.entity.Collecte import Collecte
from src.entity.Jardin import Jardin
from src.entity.User import User
from src.manager import CollecteManager
from src.manager.AdresseManager import calculerDistance2AdresseCoordonnees


def calculerDistanceParcoursListeCollecte(parcoursCollecte: list, user: User) -> int:
    parcoursToUseCollecte = parcoursCollecte.copy()
    #  On doit transformer les collectes en coordonnées
    parcoursToUseCoordTemp = transformeListeCollecteInListeCoord(parcoursToUseCollecte)

    #  On a besoin d'ajouter l'adresse de l'utilisateur
    parcoursToUseCoord = list()
    geolocUserFormatted = [-1, user.geolocLatitude, user.geolocLongitude]
    parcoursToUseCoord.append(geolocUserFormatted)

    for i in range(len(parcoursToUseCoordTemp)):
        parcoursToUseCoord.append(parcoursToUseCoordTemp[i])

    distance = calculerDistanceParcoursListeCoord(parcoursToUseCoord)

    return distance


def calculerDistanceParcoursListeCoord(parcoursCollecte: list) -> int:
    distanceTotale = 0
    lengthParcours = len(parcoursCollecte)

    if (lengthParcours > 1):
        for i in range(1, lengthParcours):
            if (i <= lengthParcours):
                collecteBeforeFormatte = parcoursCollecte[i - 1]
                collecteActualFormatte = parcoursCollecte[i]

                distanceTemp = calculerDistance2AdresseCoordonnees(collecteBeforeFormatte[1],
                                                                   collecteBeforeFormatte[2],
                                                                   collecteActualFormatte[1],
                                                                   collecteActualFormatte[2])

                distanceTotale = distanceTemp + distanceTotale

        debut = parcoursCollecte[0]
        fin = parcoursCollecte[lengthParcours - 1]

        retour = calculerDistance2AdresseCoordonnees(fin[1], fin[2], debut[1], debut[2])

        distanceTotale = distanceTotale + retour

    return distanceTotale


def meilleureInsertion(parcoursActuel: list, coordonneeFormatted: []) -> list:
    meilleurParcours = None
    meilleureDistance = 99999999999999999999999

    # On prefere tester d'ajouter a la fin plutot que debut afin d'avoir le meme point de départ
    for i in range(1, len(parcoursActuel) + 1):
        parcoursTemp = parcoursActuel.copy()

        parcoursTemp.insert(i, coordonneeFormatted)
        distanceTemp = calculerDistanceParcoursListeCoord(parcoursTemp)

        if (distanceTemp < meilleureDistance):
            meilleureDistance = distanceTemp
            meilleurParcours = parcoursTemp.copy()

    return meilleurParcours


def createFakeCollecte(user: User) -> Collecte:
    """
    Va creer une collecte et un jardin avec les coordonnées de l'utilisateur
    """
    jardinFake = Jardin(None, user.id, "", "", user.adresse)
    Mysql.db_session.add(jardinFake)
    Mysql.db_session.commit()
    collecteFake = Collecte(None, jardinFake.id, date.today(), 1)
    Mysql.db_session.add(collecteFake)
    Mysql.db_session.commit()

    return collecteFake


def dropFakeCollecte(collecteFake: Collecte):
    """
    Va suopprimer la collecte ainsi que le jardin passé en parametre
    """
    jardinFake = Jardin.query.get(collecteFake.idJardin)

    Mysql.db_session.delete(collecteFake)
    Mysql.db_session.commit()
    Mysql.db_session.delete(jardinFake)
    Mysql.db_session.commit()


def transformeListeCollecteInListeCoord(listeCollecte: list) -> list:
    """
    Renvoi une liste avec des elements de la forme :
    [idCollecte, latitude, longitude]
    """
    listeCoord = list()

    for i in range(len(listeCollecte)):
        jardin = Jardin.query.get(listeCollecte[i].idJardin)
        listeCoord.append([listeCollecte[i].id, jardin.geolocLatitude, jardin.geolocLongitude])

    return listeCoord


def transformeListeCoordinListeCollecte(listeCoord: list) -> list:
    """
    Renvoi une liste avec des elements de la forme :
    [idCollecte, latitude, longitude]
    """
    listeCollecte = list()

    for i in range(len(listeCoord)):
        idCollecte = listeCoord[i][0]

        if (idCollecte != -1):  # on filtre la geoloc utilisateur
            collecte = Collecte.query.get(idCollecte)
            listeCollecte.append(collecte)
    return listeCollecte


def getFormattedCollecteCoord(collecte: Collecte) -> []:
    jardin = Jardin.query.get(collecte.idJardin)

    return [collecte.id, jardin.geolocLatitude, jardin.geolocLongitude]


def rechercheOptimise(dateRecherche: datetime, user: User, distanceMax: int) -> list:
    """
    User va servir a recuperer sa géoloc pour en faire le point de départ
    """
    allCollecteThisDay = Collecte.query.filter_by(date=dateRecherche).all()
    allCollecteThisDay = CollecteManager.keepCollecteInscritOuDisponible(allCollecteThisDay, user)
    allCollecteThisDay = CollecteManager.keepCollecteProcheDistanceMax(allCollecteThisDay, user, distanceMax)

    geolocUserFormatted = [-1, user.geolocLatitude, user.geolocLongitude]
    parcours = list()
    parcours.append(geolocUserFormatted)

    if (len(allCollecteThisDay) > 0):
        parcours.append(getFormattedCollecteCoord(allCollecteThisDay[0]))
        allCollecteThisDay.pop(0)

        # On créé la liste de départ et on prépare la liste sur laquelle itérer
        if (len(allCollecteThisDay) > 0):
            print('taille tab collecte ', len(allCollecteThisDay), ' / ', allCollecteThisDay)
            for i in range(len(allCollecteThisDay)):
                print('Je traite un element')
                collecteActuelle = allCollecteThisDay[i]

                parcours = meilleureInsertion(parcours, getFormattedCollecteCoord(collecteActuelle))

    parcours = transformeListeCoordinListeCollecte(parcours)

    return parcours.copy()
