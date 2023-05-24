from datetime import datetime, date

from flask import render_template, session, request, redirect, url_for

from src import app
from src.database import Mysql
from src.entity.Collecte import Collecte
from src.entity.Jardin import Jardin
from src.entity.ProduitDisponible import ProduitDisponible
from src.entity.User import User


@app.route('/creation_collecte/<idJardin>', methods=['POST', 'GET'])
def creationCollecte(idJardin):
    if ('user_id' in session):
        jardin = Jardin.query.get(idJardin)
        message = ""

        user_id = session['user_id']
        user = User.query.get(user_id)

        form = request.form

        nombreEtudiant = form.get("nombreEtudiant")
        strDateCollecte = form.get("datetimeCollecte")

        if (user.typeUser == "proprietaire" and jardin != None):
            if (nombreEtudiant != None and strDateCollecte != None and jardin != None):
                if (nombreEtudiant != "" and strDateCollecte != ""):

                    datetimeCollecte = datetime.strptime(strDateCollecte, "%Y-%m-%dT%H:%M")

                    if (date.today() < datetimeCollecte):
                        if (nombreEtudiant.isnumeric()):

                            collecte = Collecte(None, jardin.id, datetimeCollecte, int(nombreEtudiant))

                            Mysql.db_session.add(collecte)
                            Mysql.db_session.commit()

                            nbProduitDispo = int(form.get("nbProduitDispo"))

                            for i in range(1, nbProduitDispo + 1):
                                print('je suis dedans avec i = ' + str(i))
                                nomProduit = form.get('nomProduit' + str(i))
                                quantiteDispo = float(form.get('quantiteProduit' + str(i)))

                                produitDispo = ProduitDisponible(None, collecte.id, nomProduit, quantiteDispo)

                                Mysql.db_session.add(produitDispo)
                                print('Ligne ProduitDispo avec id = ' + str(produitDispo.id) + ' inséré en base')

                            Mysql.db_session.commit()
                            print('Ligne Jardin avec id = ' + str(jardin.id) + ' inséré en base')

                            print('Ligne ProduitDispo avec id = ' + str(collecte.id) + ' inséré en base')

                            return redirect(url_for('userMenu'))
                        else:
                            message = "Le nombre d'étudiant doit etre un nombre"
                    else:
                        message = "Veuiller saisir une date supérieur à la date du jour"

                        return render_template('CreationCollecte.html', message=message, jardin=jardin, user=user)
                else:
                    message = "Merci de saisir tout les champs"
            return render_template('CreationCollecte.html', message=message, jardin=jardin, user=user)
        else:
            return redirect(url_for('accueil'))
    else:
        return redirect(url_for('connexionController'))
