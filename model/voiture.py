class Voiture:
    def __init__(self,
                 identifiant: int, marque: str,
                 modele: str, type_essence: str,
                 mode_de_transmission: str, numero_assurance: int,
                 id_proprietaire: int):
        self.identifiant = identifiant
        self.marque = marque
        self.modele = modele
        self.type_essence = type_essence
        self.mode_de_transmission = mode_de_transmission
        self.id_proprietaire = id_proprietaire
        self.numero_assurance = numero_assurance

    def __str__(self):
        return "[{}, ]".format()
    