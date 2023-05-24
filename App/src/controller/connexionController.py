from hashlib import sha256

from flask import render_template, session, request, redirect, url_for
from sqlalchemy import and_
from werkzeug import Response

from src import app
from src.entity.User import User


@app.route('/connexion', methods=['GET', 'POST'])
def connexionController():
    user = None
    form = request.form
    login = form.get("login")
    password = form.get("password")
    hashed_password = None

    if (password):
        hashed_password = sha256(password.encode('utf-8')).hexdigest()
        user = User.query.filter(and_(User.login == login, User.password == hashed_password)).first()

    if user != None:
        session['user_id'] = user.id
        return redirect(url_for('accueil'))

    else:
        message = ('Login introuvable')

    return render_template('connexion.html', message=message)
