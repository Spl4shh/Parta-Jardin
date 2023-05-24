from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL

from src.database.Mysql import Base


class ProduitDisponible(Base):
    __tablename__ = "produit_disponible"

    id = Column(Integer, primary_key=True)
    idCollecte = Column(Integer, ForeignKey('collecte.id'), nullable=False)
    produit = Column(String(50), nullable=False)
    quantite = Column(DECIMAL(5, 2), nullable=False)  # En Kg

    def __init__(self, id: int or None, idCollecte: int, produit: str, quantite: float):
        self.id = id
        self.idCollecte = idCollecte
        self.produit = produit
        self.quantite = quantite
