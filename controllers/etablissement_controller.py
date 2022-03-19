from models.etablissement import Etablissement
from controllers.specialite_controller import get_specialite
etablissement1 = Etablissement(1, "Clinique hotel dheli", "dehli@gmail.com", "Nyekonakpoe", "+22899595766", [get_specialite(1),get_specialite(3),get_specialite(4),get_specialite(6)])
etablissement2 = Etablissement(2, "CHU Tokoin", "tokoin@gmail.com", "Tokoin", "+22899595766", [get_specialite(2),get_specialite(4),get_specialite(5)])
etablissement3 = Etablissement(3, "CMS Sainte Joshephine Bahkita", "sjb@gmail.com", "Agoe", "+22899595766", [get_specialite(1),get_specialite(6)])
etablissement4 = Etablissement(4, "Polyclinique internationale Saint-Joseph", "pisjo@gmail.com", "Hedzranawe", "+22899595766", [get_specialite(1),get_specialite(2),get_specialite(5)])
etablissement5 = Etablissement(5, "Clinique ATBEF", "atbef@gmail.com", "Nyekonakpoe", "+22899595766", [get_specialite(3)])
etablissement6 = Etablissement(6, "CMS Ma santé", "sante@gmail.com", "Agoe", "+22899595766", [get_specialite(4),get_specialite(5),get_specialite(6)])

etablissements = [
    etablissement1.to_json(),
    etablissement2.to_json(),
    etablissement3.to_json(),
    etablissement4.to_json(),
    etablissement5.to_json(),
    etablissement6.to_json()
]


def get_all_etablissements():
    return etablissements


def get_etablissement(id):
    for etablissement in etablissements:
        if etablissement['id'] == id:
            return etablissement
    return {}
