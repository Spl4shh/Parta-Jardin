from hashlib import sha256

from flask import render_template, request, redirect, url_for

from src import app
from src.database import Mysql
from src.entity.User import User
from src.manager.AdresseManager import creerAdresse, verificationComposantesAdresse


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = request.form

    nom = form.get("nom")
    prenom = form.get("prenom")
    mail = form.get("mail")
    login = form.get("login")
    password = form.get("password")
    numAdresse = form.get("numAdresse")
    rueAdresse = form.get("rueAdresse")
    cpAdresse = form.get("cpAdresse")
    villeAdresse = form.get("villeAdresse")
    typeUser = form.get("typeUser")

    if (nom != None and prenom != None and mail != None and login != None and password != None and typeUser != None):
        if (nom != "" and prenom != "" and mail != "" and login != "" and password != "" and typeUser != ""):

            userLogin = User.query.filter_by(login = login).first()

            if ((not userLogin) and verificationComposantesAdresse(numAdresse, rueAdresse, cpAdresse, villeAdresse)):
                adresse = creerAdresse(numAdresse, rueAdresse, cpAdresse, villeAdresse)

                user = User(None, nom, prenom, mail, login, sha256(password.encode('utf-8')).hexdigest(), adresse,
                            typeUser)

                Mysql.db_session.add(user)
                Mysql.db_session.commit()
            else:
                message = "Erreur dans la saisie des informations"
                return render_template('inscription.html', message=message)
    else:
        return render_template('inscription.html')

    return redirect(url_for("connexionController"))
