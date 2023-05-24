from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, Date

from src.database.Mysql import Base


class Collecte(Base):
    __tablename__ = "collecte"

    id = Column(Integer, primary_key=True)
    idJardin = Column(Integer, ForeignKey('jardin.id'), nullable=False)
    date = Column(Date, nullable=False)
    nombreMaxEtudiants = Column(Integer, nullable=True)

    def __init__(self, id: int, idJardin: int, date: datetime, nombreMaxEtudiants: int):
        self.id = id
        self.idJardin = idJardin
        self.date = date
        self.nombreMaxEtudiants = nombreMaxEtudiants

    def __repr__(self):
        return f'<Collecte {self.id!r}>'
