from datetime import datetime, date
from typing import Any

from src.entity.Collecte import Collecte
from src.entity.InscriptionCollecte import InscriptionCollecte
from src.entity.Jardin import Jardin
from src.entity.ProduitDisponible import ProduitDisponible
from src.entity.User import User
from src.manager import AdresseManager


def listeCollecteToListeIdCollecte(listeCollecte: list) -> list:
    listeId = list()

    for i in range(len(listeCollecte)):
        listeId.append(listeCollecte[i].id)

    return listeId


def listeIdToListeCollecte(listeId: list) -> list:
    listeCollecte = list()

    for i in range(len(listeId)):
        listeCollecte.append(Collecte.query.get(listeId[i]))

    return listeCollecte


def keepCollecteInscritOuDisponible(listeCollecte: list, user: User) -> list:
    listeReturn = list()

    for i in range(len(listeCollecte)):
        collecte = listeCollecte[i]
        inscriptionUser = InscriptionCollecte.query.filter_by(idCollecte=collecte.id, idEtudiant=user.id).first()

        if (inscriptionUser):
            listeReturn.append(collecte)
        else:
            nbInscrit = InscriptionCollecte.query.filter_by(idCollecte=collecte.id).count()

            if (nbInscrit < collecte.nombreMaxEtudiants):
                listeReturn.append(collecte)

    return listeReturn

def keepCollecteAfterTodayDispoOrSub(listeCollecte: list, user: User) -> list:
    listeReturn = list()

    for i in range(len(listeCollecte)):

        collecte = listeCollecte[i]
        if (date.today() < collecte.date) :
            inscriptionUser = InscriptionCollecte.query.filter_by(idCollecte=collecte.id, idEtudiant=user.id).first()

            if (inscriptionUser):
                listeReturn.append(collecte)
            else:
                nbInscrit = InscriptionCollecte.query.filter_by(idCollecte=collecte.id).count()

                if (nbInscrit < collecte.nombreMaxEtudiants):
                    listeReturn.append(collecte)

    return listeReturn


def keepCollecteProcheDistanceMax(listeCollecte: list, user: User, distanceMax: int):
    listeReturn = list()

    for i in range(len(listeCollecte)):
        collecte = listeCollecte[i]
        jardin = Jardin.query.get(collecte.idJardin)

        distanceCollecteUser = AdresseManager.calculerDistance2AdresseCoordonnees(jardin.geolocLatitude,
            jardin.geolocLongitude, user.geolocLatitude, user.geolocLongitude)

        if (distanceCollecteUser <= distanceMax*1000) :
            listeReturn.append(collecte)

    return listeReturn


def getInfoCollectes(listeCollecte: list, user: User):
    infoCollecte = {}

    for i in range(len(listeCollecte)):
        collecte = listeCollecte[i]

        nbInscritCollecte = len(InscriptionCollecte.query.filter_by(idCollecte=collecte.id).all())
        produitsDispo = ProduitDisponible.query.filter_by(idCollecte=collecte.id).all()
        jardin = Jardin.query.filter_by(id=collecte.idJardin).first()
        dejaInscrit = (
                InscriptionCollecte.query.filter_by(idCollecte=collecte.id, idEtudiant=user.id).first() is not None)

        infoCollecte[collecte.id] = {"jardin": jardin, "nbInscription": nbInscritCollecte,
                                     "produitsDispo": produitsDispo,
                                     "dejaInscrit": dejaInscrit}

    return infoCollecte
