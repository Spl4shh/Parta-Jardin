from src.database import Mysql
from src.entity.Collecte import Collecte
from src.entity.InscriptionCollecte import InscriptionCollecte


def processActionCollecte(typeAction: str, idCollecteAction: int, user_id: int):
    if (typeAction == 'inscription'):
        nbEtuInscrit = InscriptionCollecte.query.filter_by(idCollecte=idCollecteAction).count()
        nbMax = Collecte.query.get(idCollecteAction).nombreMaxEtudiants
        if (nbEtuInscrit >= nbMax):
            message = "Il y a déjà trop d'inscrits"
        else:
            Mysql.db_session.add(InscriptionCollecte(idCollecteAction, user_id))
            Mysql.db_session.commit()

    elif (typeAction == 'desinscription'):
        inscription = InscriptionCollecte.query.filter_by(idCollecte=idCollecteAction, idEtudiant=user_id).first()
        if (inscription):
            Mysql.db_session.delete(inscription)
            Mysql.db_session.commit()
