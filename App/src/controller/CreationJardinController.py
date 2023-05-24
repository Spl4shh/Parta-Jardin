from flask import render_template, session, request, redirect, url_for

from src.manager.AdresseManager import creerAdresse, verificationComposantesAdresse
from src.database import Mysql
from src import app
from src.entity.Jardin import Jardin
from src.entity.User import User


@app.route('/creation_jardin', methods=['POST', 'GET'])
def creationJardin():

    if ('user_id' in session):
        message = ""

        user_id = session['user_id']
        user = User.query.get(user_id)

        if (user and user.typeUser == 'proprietaire'):

            form = request.form

            numAdresse = form.get("numAdresse")
            rueAdresse = form.get("rueAdresse")
            cpAdresse = form.get("cpAdresse")
            villeAdresse = form.get("villeAdresse")
            description = form.get("description")
            lienImage = form.get("lienImage")


            if (numAdresse != None and rueAdresse != None and cpAdresse != None and villeAdresse != None and description != None):
                if (numAdresse != "" and rueAdresse != "" and cpAdresse != "" and villeAdresse != "" and description != ""):
                    if(verificationComposantesAdresse(numAdresse, rueAdresse, cpAdresse, villeAdresse)):

                        # Suppression des espaces inutiles uniquement si nécéssaire
                        description = description.strip()
                        lienImage = lienImage.strip()

                        adresse = creerAdresse(numAdresse, rueAdresse, cpAdresse, villeAdresse)

                        if (lienImage == ""):
                            lienImage = "/static/image/placeholder.jpg"

                        jardin = Jardin(None, user.id, description, adresse, lienImage)

                        Mysql.db_session.add(jardin)
                        Mysql.db_session.commit()

                        return redirect(url_for('userMenu'))
                    else:
                        message = "Erreur dans la saisie de l'adresse"
                else:
                    message = "Merci de saisir tout les champs"
            return render_template('CreationJardin.html',  message = message,user=user)
        else:
            return redirect(url_for('accueil'))
    else:
        return redirect(url_for('connexionController'))
