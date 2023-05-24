import json
import urllib.parse
from math import sin, cos, acos, pi

import requests as requests


# Verifie les differents champs composant une adresse
def verificationComposantesAdresse(numAdresse: str, rueAdresse: str, cpAdresse: str, villeAdresse: str):
    return (
            numAdresse.strip() != "" and rueAdresse.strip() != "" and cpAdresse.strip() != "" and villeAdresse.strip() != "" and
            numAdresse.isnumeric() and
            not rueAdresse.isnumeric() and
            cpAdresse.isnumeric() and 4 <= len(cpAdresse.strip()) <= 5 and
            not villeAdresse.isnumeric())


# Renvoi un string contenant l'adresse de la forme :
# Numero Rue, CodePostal Ville
def creerAdresse(numAdresse: str, rueAdresse: str, cpAdresse: str, villeAdresse: str):
    if (verificationComposantesAdresse(numAdresse, rueAdresse, cpAdresse, villeAdresse)):
        if (len(cpAdresse.strip()) == 4):
            cpAdresse = "0" + cpAdresse.strip()

        return numAdresse.strip() + " " + rueAdresse.strip() + ", " + cpAdresse.strip() + " " + villeAdresse.strip()
    else:
        return "Erreur lors de la cretion de l'adresse"


# Return de la forme :
# [0: Lattitude, 1: Longitude]
def transformerAdresseToGeoloc(adresse: str):
    api_url = "https://api-adresse.data.gouv.fr/search/?q="
    r = requests.get(api_url + urllib.parse.quote(adresse))

    objJson = json.loads(r.content.decode('unicode_escape'))
    coordonnees = {'longitude': objJson["features"][0]["geometry"]["coordinates"][0],
                   'latitude': objJson["features"][0]["geometry"]["coordinates"][1]}

    return coordonnees


def calculerDistance2AdresseCoordonnees(latitudeA: float, longitudeA: float, latitudeB: float, longitudeB: float):
    def distanceGPS(laA, loA, laB, loB):
        """Retourne la distance en mètres entre les 2 points A et B connus grâce à
           leurs coordonnées GPS (en radians).
        """
        # Rayon de la terre en mètres
        RT = 6378137
        # angle en radians entre les 2 points

        S = acos(sin(laA) * sin(laB) + cos(laA) * cos(laB) * cos(abs(loB - loA)))
        # distance entre les 2 points, comptée sur un arc de grand cercle
        return S * RT

    def deg2rad(dd):
        """Convertit un angle "degrés décimaux" en "radians"
        """
        return float(dd) / 180 * pi

    latA = deg2rad(latitudeA)  # Nord
    longA = deg2rad(longitudeA)  # Est

    latB = deg2rad(latitudeB)  # Nord
    longB = deg2rad(longitudeB)  # Est

    return distanceGPS(latA, longA, latB, longB)
