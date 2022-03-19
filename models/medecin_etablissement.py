from models.medecin import Medecin
from models.etablissement import Etablissement
from controllers.medecin_controller import get_medecin
from controllers.etablissement_controller import get_etablissement


class MedecinEtablissements(Medecin, Etablissement):
    def __init__(self, medecin_id: int, etablissement_id: int, disponibilite):
        current_med = get_medecin(medecin_id)
        current_et = get_etablissement(etablissement_id)
        Medecin.__init__(self,current_med["utilisateur"], current_med["titre"], current_med["profession"],
                         current_med["formations"], current_med["experiences"], current_med["presentation"],
                         current_med["langues"], current_med["actes"])
        Etablissement.__init__(self,current_et["id"], current_et["nom"], current_et["email"], current_et["adresse"],
                               current_et["contact"], current_et["actes"])
        self.disponibilite = disponibilite

    def to_json(self):
        dictionnaire = {
            "medecin": Medecin.to_json(self),
            "etablissement": Etablissement.to_json(self),
            "disponibilite": self.disponibilite
        }
        return dictionnaire
