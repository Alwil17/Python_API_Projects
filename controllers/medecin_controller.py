from models.medecin import Medecin
from controllers.utilisateur_controller import get_user
from controllers.specialite_controller import get_specialite

medecin1 = Medecin(get_user(3), "Dr", "Pediatre", {"2019-2020": "Ecole de medecine de Paris"},
                   {"2020-2021": "Clinique Saint joseph"}, "Gentile et doux", "Anglais",
                   [get_specialite(2), get_specialite(3)])
medecin2 = Medecin(get_user(5), "Dr", "Pediatre", {"2019-2020": "Ecole de medecine de Vienne"},
                   {"2020-2021": "Clinique Saint joseph"}, "Gentile et doux", "Anglais",
                   [get_specialite(1), get_specialite(3), get_specialite(4)])
medecin3 = Medecin(get_user(6), "Dr", "Pediatre", {"2019-2020": "Ecole de medecine de Rome"},
                   {"2020-2021": "Clinique Saint joseph"}, "Gentile et doux", "Anglais",
                   [get_specialite(4), get_specialite(5)])

medecins = [
    medecin1.to_json(),
    medecin2.to_json(),
    medecin3.to_json(),
]


def get_all_medecins():
    return medecins


def get_medecin(id):
    for medecin in medecins:
        if medecin["utilisateur"]['id'] == id:
            return medecin
    return {}
