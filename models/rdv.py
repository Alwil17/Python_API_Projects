from models.etablissement import Etablissement
from models.medecin import Medecin
from models.patient import Patient


class RDV(Patient,Medecin,Etablissement):
    def __init__ (self,id:int,motifs:str,heure:str,actes):
        self.id = id
        self.patient_id = Patient.id
        self.medecin_id = Medecin.id
        self.etablissement_id = Etablissement.id
        self.motifs = motifs
        self.heure = heure
        self.actes = actes
    