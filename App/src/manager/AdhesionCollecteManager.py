from sqlalchemy import or_
from src.database import Mysql
from src import app
from src.entity.Jardin import Jardin
from src.entity.Collecte import Collecte
from src.entity.InscriptionCollecte import InscriptionCollecte
from src.entity.User import User
from src.entity.ProduitDisponible import  ProduitDisponible


def InfoCollecte(collectes,user):
    collectes_data_sended_to_html = []
    for collecte in collectes:
        # Recupération des differentes données
        nb_etu_inscrit = InscriptionCollecte.query.filter_by(idCollecte=collecte.id).count()
        deja_inscrit = InscriptionCollecte.query.filter_by(idCollecte=collecte.id,
                                                           idEtudiant=user.id).first()
        deja_inscrit = True if deja_inscrit else False  # Opérateur ternaire, si déjà inscrit alors true, sinon false
        jardin_collecte = Jardin.query.get(collecte.idJardin)
        proprietaire_jardin = User.query.get(jardin_collecte.idProprietaire)
        produits_dispo_collecte = ProduitDisponible.query.filter(
            ProduitDisponible.idCollecte == collecte.id).all()

        liste_produit = []
        for i in produits_dispo_collecte:
            liste_produit.append({"produit": i.produit, "quantite": i.quantite})

        # Ajout dans un unique tableau
        collectes_data_sended_to_html.append({"id": collecte.id,
                                              "id_jardin": collecte.idJardin,
                                              "nom_proprietaire": proprietaire_jardin.nom,
                                              "prenom_proprietaire": proprietaire_jardin.prenom,
                                              "adresse_jardin": jardin_collecte.adresseJardin,
                                              "image_jardin": jardin_collecte.image,
                                              "description_jardin": jardin_collecte.description,
                                              "nombre_etu_max": collecte.nombreMaxEtudiants,
                                              "nombre_etu_inscrit": nb_etu_inscrit,
                                              "date": collecte.date.strftime("%d/%m/%Y"),
                                              "produit_disponible": liste_produit,
                                              "deja_inscrit": deja_inscrit})
    return collectes_data_sended_to_html