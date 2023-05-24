from flask import session, redirect, url_for

from src import app
from src.database import Mysql
from src.entity.Collecte import Collecte
from src.entity.InscriptionCollecte import InscriptionCollecte
from src.entity.Jardin import Jardin
from src.entity.ProduitDisponible import ProduitDisponible
from src.entity.User import User


@app.route('/user/delete', methods=['GET'])
def deleteUser():
    user_id = session['user_id']

    allInscriptionCollecte = InscriptionCollecte.query.filter_by(idEtudiant=user_id).all()
    for i in range(len(allInscriptionCollecte)):
        inscription = allInscriptionCollecte[i]

        Mysql.db_session.delete(inscription)
        Mysql.db_session.commit()

    allJardin = Jardin.query.filter_by(idProprietaire=user_id).all()
    for i in range(len(allJardin)):
        jardin = allJardin[i]

        allCollecte = Collecte.query.filter_by(idJardin=jardin.id).all()
        for j in range(len(allCollecte)):
            collecte = allCollecte[j]

            allProduitDispo = ProduitDisponible.query.filter_by(idCollecte=collecte.id).all()
            for h in range(len(allProduitDispo)):
                produitDispo = allProduitDispo[h]
                Mysql.db_session.delete(produitDispo)
                Mysql.db_session.commit()

            allInscriptionCollecte = InscriptionCollecte.query.filter_by(idCollecte=collecte.id).all()
            for k in range(len(allInscriptionCollecte)):
                inscription = allInscriptionCollecte[k]

                Mysql.db_session.delete(inscription)
                Mysql.db_session.commit()

            Mysql.db_session.delete(collecte)
            Mysql.db_session.commit()

        Mysql.db_session.delete(jardin)
        Mysql.db_session.commit()

    user = User.query.get(user_id)

    if (user):
        Mysql.db_session.delete(user)
        Mysql.db_session.commit()

    return redirect(url_for('inscription'))
