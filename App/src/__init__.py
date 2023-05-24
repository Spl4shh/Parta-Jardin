from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from src.database.Mysql import DB_URL_CONNECTION, initDatabase
from flask_fontawesome import FontAwesome
from werkzeug.routing import Rule

initDatabase()
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL_CONNECTION
db.init_app(app)
fa = FontAwesome(app)
app.secret_key = 'SecretKeyOfTheApp'

# Traitement des routes inconnues, redirection vers la page d'accueil automatique
app.url_map.add(Rule("/", defaults={"_404": ""}, endpoint="catch_all"))
app.url_map.add(Rule("/<path:_404>", endpoint="catch_all"))


@app.endpoint("catch_all")
def _404(_404):
    return redirect(url_for("accueil"))


from src.controller import RechercheOptimiseController
from src.controller import UserMenuController
from src.controller import CreationJardinController
from src.controller import AdhesionCollecteController
from src.controller import CreationCollecteController
from src.controller import VisualisationJardinController
from src.controller import DeleteUserController
from src.controller import inscriptionController
from src.controller import ListeCollecteFromJardinController
from src.controller import connexionController
from src.controller import deconnexionController
from src.controller import accueilController
