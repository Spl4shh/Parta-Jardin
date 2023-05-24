from sqlalchemy import Column, Integer, String

from src.database.Mysql import Base
from src.manager import AdresseManager


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    mail = Column(String(100), nullable=False)
    login = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    typeUser = Column(String(50), nullable=False)  # proprietaire ou etudiant
    adresse = Column(String(100), nullable=False)
    geolocLatitude = Column(String(100), nullable=False)
    geolocLongitude = Column(String(100), nullable=False)

    def __init__(self, id: int, nom: str, prenom: str, mail: str, login: str, password: str, adresse: str,
                 typeUser: str) -> object:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.login = login
        self.password = password
        self.typeUser = typeUser
        self.adresse = adresse
        coordonnees = AdresseManager.transformerAdresseToGeoloc(adresse)
        self.geolocLatitude = coordonnees['latitude']
        self.geolocLongitude = coordonnees['longitude']
