from flask import session, redirect, url_for

from src import app


@app.route('/deconnexion', methods=['POST', 'GET'])
def deconnexion():
    # Supprimer la session de l'utilisateur
    session.pop('user_id', None)
    return redirect(url_for('accueil'))
