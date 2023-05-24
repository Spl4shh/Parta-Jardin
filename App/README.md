Pour lancer le projet, vous devez installer une base de donnée MySQL (En utilisant Xampp par exemple : [Lien vers XAMPP](https://www.apachefriends.org/fr/index.html)), puis autoriser la police d'execution
(Set-ExecutionPolicy AllSigned). Vous devez lancer un terminal en mode administrateur puis executer cette commande.
Enfin il vous suffira de copier coller le contenu de initProject.sh et de le coller dans une console dédié au même endroit que ce dossier.
Enfin une fois l'ensemble des commandes executés, il faudra faire entrée et votre application sera lancée

Créer l'environnement virtuel
```shell
py -m venv venv
```
ou
```shell
python3 -m venv venv
```

Autoriser les scripts sous powershell puis activer l'environnement
```shell
Set-ExecutionPolicy AllSigned
.\venv\Scripts\activate
```

Installer Flask
```shell
pip install Flask
```

Installer SQLalchemy
```shell
pip install -U Flask-SQLAlchemy
```

Sauvegarder les prérequis pour votre environnement
```shell
pip freeze > requirements.txt
```

Installer des packages depuis le fichier de prérequis
```shell
pip install -r requirements.txt
```

Veuillez lancer un serveur MySQL (voir #Base de Données)
Pour lancer le serveur : (/!\ Attention, il faut etre dans le dossier de app.py)
```shell
$env:FLASK_APP = "app.py"
flask run
```



## Conseil : 

### Base de Données :
Veuillez utiliser une base de données MySQL (Xampp par exemple). Il suffira de lancer le serveur MySQL. Le projet a été configuré pour contenir des données dès son lancement, la base sera elle aussi automatiquement créée.

### Routes : 
Actuellement toutes les routes sont dans le fichier app.py.
Possible de mettre les routes dans les "controller"

### Controller template :
Utiliser une methode xxxController afin de ne pas tout avoir dans un fichier

### Variables :
Pour les variables passé à ces fonctions, les passer sous forme de liste ou de tableau afin de pouvoir les modifier dans
la fonction. A moins que ce ne soit des tableaux de base, ces variables transformé en tableau ne contiendront qu'un seul 
élément

### Component :
https://stackoverflow.com/a/55844364

### Commande git :
Pour merge master dans sa branche : 
```git
git fetch
git rebase origin/master 
# Si vous ne voulez pas de commit de merge

git fetch
git merge origin/master
# Si vous voulez un commit de merge
```
