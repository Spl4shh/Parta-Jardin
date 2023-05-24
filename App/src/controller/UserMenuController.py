from datetime import date

from flask import render_template, session, redirect, url_for

from src import app
from src.entity.Collecte import Collecte
from src.entity.InscriptionCollecte import InscriptionCollecte
from src.entity.Jardin import Jardin
from src.entity.User import User


@app.route('/menu')
def userMenu():
    collectesUserCourant = []
    jardins = []
    jardinsCollecte = {}

    if ('user_id' in session):
        user_id = session['user_id']
        user = User.query.get(user_id)

        if (user.typeUser == 'proprietaire'):
            jardins = Jardin.query.filter_by(idProprietaire=user.id).all()
        else:  # type Etudiant
            listeInscription = InscriptionCollecte.query.filter_by(idEtudiant=user.id).all()

            for inscription in listeInscription:
                collecte = Collecte.query.filter_by(id=inscription.idCollecte).first()
                if (collecte.date > date.today()):
                    collectesUserCourant.append(collecte)

            jardins = [0] * len(listeInscription)

            for collecte in collectesUserCourant:
                jardinsCollecte[collecte.idJardin] = Jardin.query.get(collecte.idJardin)

        return render_template('UserMenu.html', user=user, jardins=jardins, collectesUserCourant=collectesUserCourant,
                               jardinsCollecte=jardinsCollecte)
    else:
        return redirect(url_for('accueil'))
