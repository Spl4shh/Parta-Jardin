from flask import render_template, session, url_for

from src import app
from src.entity.Collecte import Collecte
from src.entity.Jardin import Jardin
from src.entity.User import User


@app.route('/jardin/<idJardin>')
def jardin(idJardin):
    if ('user_id' in session):
        message = ""
        user_id = session['user_id']
        user = User.query.get(user_id)
        if (user):
            jardin = Jardin.query.get(idJardin)
            proprietaire = User.query.get(jardin.id)
            collectes = Collecte.query.filter_by(idJardin=idJardin).first()
            voir_col = False
            if (collectes):
                voir_col = True

            return render_template('jardin.html', jardin=jardin, proprietaire=proprietaire, collectes=voir_col,
                                   user=user)
        return 'Utilisateur inconnu'
    else:
        return render_template(url_for('connexionController'))  # devra etre connexion
