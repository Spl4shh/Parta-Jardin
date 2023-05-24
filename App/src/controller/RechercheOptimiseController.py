from datetime import datetime, date

from flask import render_template, session, request, redirect, url_for

from src import app
from src.entity.User import User
from src.manager import CollecteManager, InscriptionCollecteManager
from src.manager import RechercheOptimiseManager
from src.manager.CollecteManager import getInfoCollectes


@app.route('/recherche_optimise', methods=['POST', 'GET'])
def rechercheOptimise():
    user_id = session['user_id']

    ordreOptimise = list()
    infoCollecte = {}
    distanceTotale = 0

    form = request.form

    dateDuJour = date.today()
    dateRecherche = form.get('dateRecherche')
    btnRecherche = form.get('recherche')
    typeAction = form.get('type')
    distanceMax = form.get('distanceMax')
    idCollecteAction = form.get('collecte_id')

    if ('user_id' in session):
        user = User.query.get(user_id)
        if (user.typeUser == 'etudiant'):
            if (btnRecherche != None and dateRecherche != None and dateRecherche != ''):
                dateUsable = datetime.strptime(dateRecherche, "%Y-%m-%d")
                distanceMax = int(distanceMax)

                session['ordreOptimiseId'] = None
                ordreOptimise = RechercheOptimiseManager.rechercheOptimise(dateUsable, user, distanceMax)
                session['ordreOptimiseId'] = CollecteManager.listeCollecteToListeIdCollecte(ordreOptimise)

            elif (typeAction != None):
                idCollecteAction = int(idCollecteAction)

                #  Traitement pour l'inscription
                InscriptionCollecteManager.processActionCollecte(typeAction, idCollecteAction, user.id)

                #  Traitement pour la liste Optimisé
                listeIdOrdreOptimise = session['ordreOptimiseId']
                ordreOptimise = CollecteManager.listeIdToListeCollecte(listeIdOrdreOptimise)

            if (typeAction != None or btnRecherche != None):
                distanceTotale = round(
                    RechercheOptimiseManager.calculerDistanceParcoursListeCollecte(ordreOptimise, user) / 1000, 2)

            infoCollecte = getInfoCollectes(ordreOptimise, user)

            trajet = "https://www.google.com/maps/dir/"
            trajet += user.geolocLatitude + "," + user.geolocLongitude + "/"
            for collecte in ordreOptimise:
                # if (infoCollecte[collecte.id]['nbInscription'] < collecte.nombreMaxEtudiants or infoCollecte[collecte.id]['dejaInscrit']):
                trajet += infoCollecte[collecte.id]['jardin'].geolocLatitude + "," + infoCollecte[collecte.id][
                    'jardin'].geolocLongitude + "/"
            trajet += user.geolocLatitude + "," + user.geolocLongitude + "/"
            trajet += "data=!4m2!4m1!3e1"

            return render_template('RechercheOptimise.html', ordreOptimise=ordreOptimise, infoCollecte=infoCollecte,
                                   dateRecherche=dateRecherche, message="", dateDuJour=dateDuJour,
                                   distanceTotale=distanceTotale, trajet=trajet, user=user)

    return redirect(url_for('accueil'))
