from flask import Flask, render_template, request, session
from src import app
from src.entity.User import User

@app.route('/accueil')
def accueil():
    user = None
    if ('user_id' in session):
        
        user_id = session['user_id']
        user = User.query.get(user_id)
        
    return render_template('accueil.html', user = user)
