from flask import render_template, session, url_for, redirect

from src import app
from src.entity.Collecte import Collecte
from src.entity.Jardin import Jardin
from src.entity.User import User
from src.manager.CollecteManager import getInfoCollectes, keepCollecteAfterTodayDispoOrSub


@app.route('/liste_collecte/<idJardin>/')
def listeCollecte(idJardin):
    collectesJardinCourant = []
    jardin = Jardin.query.get(idJardin)

    if ('user_id' in session and jardin):
        user_id = session['user_id']
        user = User.query.get(user_id)

        if (user != None and user.typeUser == 'proprietaire'):
            if (jardin.idProprietaire == user.id):
                collectes = Collecte.query.filter_by(idJardin=jardin.id).all()
                collectes = keepCollecteAfterTodayDispoOrSub(collectes, user)
                infoCollectes = getInfoCollectes(collectes, user)

                return render_template('ListeCollecteFromJardin.html', jardin=jardin, collectes=collectes, user=user,
                                       infoCollectes=infoCollectes)

    return redirect(url_for('userMenu'))
