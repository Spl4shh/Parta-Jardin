from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from hashlib import sha256
from sqlalchemy_utils import database_exists, create_database

DB_URL_CONNECTION = 'mysql+pymysql://root:@localhost:3306/ppii_db'
engine = create_engine('mysql+pymysql://root:@localhost:3306/ppii_db')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# Build + add Content
def initDatabase():
    if not database_exists(engine.url):
        create_database(engine.url)
        buildDatabase()


def buildDatabase():
    import src.entity.User
    import src.entity.Jardin
    import src.entity.ProduitDisponible
    import src.entity.Collecte
    import src.entity.InscriptionCollecte

    Base.metadata.create_all(bind=engine)
    addContentIntoDatabase()


def addContentIntoDatabase():
    #passwords visibles pour le test uniquement, utilisez les pour tester les users
    formatuser = ['id', 'nom', 'prenom', 'mail', 'login', 'password', 'adresse', 'typeUser', 'geolocLatitude', 'geolocLongitude']
    datauser = [(1, 'Renard', 'Nicolas', 'nicolas.renard@telecomnancy.eu', 'renardlog', sha256("password".encode('utf-8')).hexdigest(),
                 '193 Avenue Paul Muller 54600 Villers les Nancy', 'etudiant', 48.669132, 6.155745),
                (2, 'Natanelic', 'Romain', 'romain.natanelic@telecomnancy.eu', 'romainlog', sha256("password".encode('utf-8')).hexdigest(),
                 '96 Rue du moitrier, 54600 Villers les Nancy', 'proprietaire', 48.671064, 6.151197),
                (3, 'Gehin', 'Clement', 'clement.gehin@telecomnancy.eu', 'clementlog', sha256("password".encode('utf-8')).hexdigest(),
                 '4 Rue Saint Fiacre, 54600 Villers-lès-Nancy', 'etudiant', 48.668831, 6.144902),
                (4, 'Courrier', 'Louis', 'courrier.louis@telecomnancy.eu', 'louislog', sha256("87Aaasd".encode('utf-8')).hexdigest(),
                 '2 Rue d\'Armorique, 54425 Pulnoy', 'proprietaire', 48.699530, 6.258695),
                (5, 'Jean', 'Michel', 'jean.michel@telecomnancy.eu', 'jmlog', sha256("jmpassword".encode('utf-8')).hexdigest(),
                 '49 Rue Sainte-Colette, 54500 Vandoeuvre-les-Nancy', 'etudiant', 48.676578, 6.186140)
                ]

    formatjardin = ['id', 'idProprietaire', 'description', 'adresseJardin', 'image', 'geolocLatitude', 'geolocLongitude']
    datajardin = [(1, 2, 'beaucoup de raisin par ici', '74 Avenue de la Malgrange, 54140 Jarville-la-Malgrange',
                   "/static/image/placeholder.jpg", 48.666148, 6.197713),
                  (2, 2, 'beaucoup de pommes par ici et un peu de raisin', '4 Rue de la République, 54320 Maxéville',
                   "https://www.lesentreprisesdupaysage.fr/content/uploads/2022/03/5996742323_3aa33bfa07_b.jpg", 48.712786, 6.162816),
                  (3, 4, 'Les recoltes joyeuses de Louis', '2 Rue d\'Armorique, 54425 Pulnoy',
                   "https://www.consoglobe.com/wp-content/uploads/2021/06/jardins-du-mode_shutterstock_106345766.jpg", 48.699530, 6.258695),
                  ]

    formatcollecte = ['id', 'idJardin', 'date', 'nombreMaxEtudiants']
    datacollecte = [(1, 1, '2022-11-27', 2),
                    (2, 1, '2022-12-30', 20),
                    (3, 2, '2023-12-02', 15),
                    (4, 3, '2023-01-21', 3),
                    (5, 2, '2023-01-21', 1),
                    (6, 1, '2023-01-21', 12)]

    formatproduit_disponible = ['id', 'idCollecte', 'produit', 'quantite']
    dataproduit_disponible = [(1, 1, 'Raisin', 2.50),
                              (2, 2, 'Raisin', 10.00),
                              (3, 3, 'Pommes', 7.50),
                              (4, 4, 'Poires', 2.00),
                              (5, 5, 'Tomates', 3.50),
                              (6, 5, 'Cerise', 10.50),
                              (7, 5, 'Celeris', 1.50),
                              (8, 6, 'Abricot', 2.00)]

    formatinscription_collecte = ['idCollecte', 'idEtudiant']
    datainscription_collecte = [(1, 1),
                                (1, 3),
                                (2, 3),
                                (3, 1),
                                (6, 1),
                                (4, 5),
                                (6, 5)]

    add_data_to_table(table="user", format=formatuser, data=datauser)
    add_data_to_table(table="jardin", format=formatjardin, data=datajardin)
    add_data_to_table(table="collecte", format=formatcollecte, data=datacollecte)
    add_data_to_table(table="produit_disponible", format=formatproduit_disponible, data=dataproduit_disponible)
    add_data_to_table(table="inscription_collecte", format=formatinscription_collecte, data=datainscription_collecte)


def add_data_to_table(table, format, data):
    args = ''
    for i in format:
        args += '%s,'
    try:
        query = "INSERT INTO " + table + " (" + ','.join(format) + ") VALUES (" + args[:-1] + ")"
        id = engine.execute(query, data)
        print("Rangs ajoutés : ", id.rowcount, " dans la table : ", table)
    except:
        print("Database error ")



# Pour faire une requete : 
# peter = ENTITY_CONCERNED.query.filter_by(ATTRIBUTE='peter').first() ou .all()
# peter = ENTITY_CONCERNED.query.get(ID)
#
# Importer la variable db de Mysql.py
#
#
# Mysql.db_session.add(VAR)
# ou
# Mysql.db_session.delete(VAR)
# finir par 
# Mysql.db_session.commit()
