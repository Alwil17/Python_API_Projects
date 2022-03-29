import time

from geopy.geocoders import Nominatim
from geopy import distance

# Vous devez changet le nom du projet
app = Nominatim(user_agent="rdv_medical")


def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)


def get_address_by_location(latitude, longitude, language="en"):
    coordinates = f"{latitude}, {longitude}"
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)


def calculate_distance_between(pointa, pointb):
    """Cette methode calcule la distance entre deux points a et b.
    Les distances sont des tuples de latitude et longitude.
    Exemple: pointa = (lat, lon)"""
    time.sleep(1)
    try:
        return distance.distance(pointa, pointb)
    except:
        return calculate_distance_between(pointa, pointb)


def get_shprten_distance_between(pointa, entities):
    """Calcule et selectionne la plus petite distance entre un point a
    et une liste d'autres objects contenant des localisations.
    On suppose que le dictionnaire addresses est de la forme:
    entities = [{
      "id": key,
      ....
      "localisation": {
          "lat": "1.125544",
          "lon": "-13.2555"
      }
    }, {
      "id": key,
       ...,
       "localisation": {
          "lat": "1.125544",
          "lon": "-13.2555"
      }}]"""
    # stock un dicttionnaire contenant l'intitulé de l'adresse et la distance
    distances = []
    for address in entities:
        pointb = (address["localisation"]["lat"], address["localisation"]["lon"])
        final_distance = calculate_distance_between(pointa, pointb)
        data_to_add = {"id": address["id"], "diatance": final_distance}
        distances.append(data_to_add)

    return distances
