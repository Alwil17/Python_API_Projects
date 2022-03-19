from models.specialite import Specialite

specialite1 = Specialite(1, "Pediatrie")
specialite2 = Specialite(2, "Gynecologie")
specialite3 = Specialite(3, "Ophtalmologie")
specialite4 = Specialite(4, "Rhumatologie")
specialite5 = Specialite(5, "Dermatologie")
specialite6 = Specialite(6, "Cardiologie")
specialite7 = Specialite(7, "Urologie")

specialites = [
    specialite1.to_json(),
    specialite2.to_json(),
    specialite3.to_json(),
    specialite4.to_json(),
    specialite5.to_json(),
    specialite6.to_json(),
    specialite7.to_json()
]


def get_all_specialites():
    return specialites


def get_specialite(id):
    for specialite in specialites:
        if specialite['id'] == id:
            return specialite
    return {}


def store_specialite(specialite):
    specialites.append(specialite)
