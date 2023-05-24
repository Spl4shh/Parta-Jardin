from sqlalchemy import Column, ForeignKey, Integer

from src.database.Mysql import Base


class InscriptionCollecte(Base):
    __tablename__ = "inscription_collecte"

    idCollecte = Column(Integer, ForeignKey('collecte.id'), primary_key=True)
    idEtudiant = Column(Integer, ForeignKey('user.id'), primary_key=True)

    def __init__(self, idCollecte: int, idEtudiant: int):
        self.idCollecte = idCollecte
        self.idEtudiant = idEtudiant
