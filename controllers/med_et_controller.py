from models.medecin_etablissement import MedecinEtablissements

medecin1 = MedecinEtablissements(3, 6, {"Lundi": ["08h-10h","14h-17h"]})
medecin2 = MedecinEtablissements(5, 6, {"Mardi": ["11h-13h"]})
medecin3 = MedecinEtablissements(6, 3, {"Jeudi": ["08h-12h"]})

medecins = [
    medecin1.to_json(),
    medecin2.to_json(),
    medecin3.to_json()
]

def get_medecin_in_etablissement(id):
    founded_meds = []
    for medecin in medecins:
        if medecin["etablissement"]['id'] == id:
            dictionnaire = {
                "medecin": medecin["medecin"],
                "disponibilite": medecin["disponibilite"]
            }
            founded_meds.append(dictionnaire)
    return founded_meds
