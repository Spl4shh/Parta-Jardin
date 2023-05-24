from datetime import date

from flask import render_template, session, request, redirect, url_for
from sqlalchemy import or_, and_

from src import app
from src.database import Mysql
from src.entity.Collecte import Collecte
from src.entity.InscriptionCollecte import InscriptionCollecte
from src.entity.Jardin import Jardin
from src.entity.ProduitDisponible import ProduitDisponible
from src.entity.User import User
from src.manager.AdhesionCollecteManager import InfoCollecte


@app.route('/adhesion_collecte', methods=['POST', 'GET'])
def adhesionCollecte():
    if ('user_id' in session):
        message = ""

        user_id = session['user_id']
        user = User.query.get(user_id)
        if (user and user.typeUser == 'etudiant'):
            if request.method == 'POST':
                form = request.form.to_dict()
                if (form['type'] == 'inscription'):
                    nb_etu_inscrit = InscriptionCollecte.query.filter_by(idCollecte=form['collecte_id']).count()
                    nb_max = Collecte.query.get(form['collecte_id']).nombreMaxEtudiants
                    if (nb_etu_inscrit >= nb_max):
                        message = "Il y a déjà trop d'inscrits"
                    else:
                        Mysql.db_session.add(InscriptionCollecte(int(form['collecte_id']), user_id))
                        Mysql.db_session.commit()
                    return redirect(url_for('adhesionCollecte'))  # Réinitialisation du form
                elif (form['type'] == 'desinscription'):
                    instance = InscriptionCollecte.query.filter_by(idCollecte=form['collecte_id'],
                                                                   idEtudiant=user_id).first()
                    if (instance):
                        Mysql.db_session.delete(instance)
                        Mysql.db_session.commit()
                    return redirect(url_for('adhesionCollecte'))  # Réinitialisation du form
                elif (form['type'] == 'recherche'):
                    arguments = form['barre_recherche'].split(',')
                    if (len(arguments) == 1):
                        arguments.append('')

                    collectes = Collecte.query.join(Jardin, Collecte.idJardin == Jardin.id). \
                        join(ProduitDisponible, ProduitDisponible.idCollecte == Collecte.id). \
                        filter(or_(and_(Jardin.adresseJardin.like('%' + arguments[0] + '%'),
                                        ProduitDisponible.produit.like('%' + arguments[1] + '%')),
                                   and_(Jardin.adresseJardin.like('%' + arguments[1] + '%'),
                                        ProduitDisponible.produit.like('%' + arguments[0] + '%')))). \
                        filter(Collecte.idJardin == Jardin.id). \
                        filter(Collecte.id == ProduitDisponible.idCollecte). \
                        filter(Collecte.date > date.today())

                    collectes_data_sended_to_html = InfoCollecte(collectes, user)

                    return render_template('AdhesionCollecte.html', message=message,
                                           collectes=collectes_data_sended_to_html, user=user)

            collectes = Collecte.query.filter(Collecte.date > date.today()).all()
            collectes_data_sended_to_html = InfoCollecte(collectes, user)

            return render_template('AdhesionCollecte.html', message=message, collectes=collectes_data_sended_to_html,
                                   user=user)
        return redirect(url_for('accueil'))
    else:
        return redirect(url_for('connexionController'))
