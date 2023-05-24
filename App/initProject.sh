# A coller dans sa console à chaque démarrage
py -m venv venv
Set-ExecutionPolicy AllSigned
.\venv\Scripts\activate
pip install -r requirements.txt
$env:FLASK_APP = "app.py"
flask --debug run