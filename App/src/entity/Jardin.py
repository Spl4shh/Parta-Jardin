from sqlalchemy import Column, ForeignKey, String, Integer
from src.database.Mysql import Base
from src.manager import AdresseManager


class Jardin(Base):
    __tablename__ = "jardin"

    id = Column(Integer, primary_key=True)
    idProprietaire = Column(Integer, ForeignKey('user.id'), nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(String(100), nullable=True)  # Lien http de l'image à afficher
    adresseJardin = Column(String(255), nullable=False)
    geolocLatitude = Column(String(100), nullable=False)
    geolocLongitude = Column(String(100), nullable=False)

    def __init__(self, id: int or None, idProprietaire: int, description: str, adresseJardin: str, image: str):
        self.id = id
        self.idProprietaire = idProprietaire
        self.description = description
        self.image = image
        self.adresseJardin = adresseJardin
        coordonnees = AdresseManager.transformerAdresseToGeoloc(adresseJardin)
        self.geolocLatitude = coordonnees['latitude']
        self.geolocLongitude = coordonnees['longitude']
