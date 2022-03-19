from models.utilisateur import Utilisateur


class Medecin(Utilisateur):
    def __init__(self, utilisateur, titre: str, profession: str, formations, experiences, presentation,
                 langues, actes):
        super().__init__(utilisateur["id"], utilisateur["nom"], utilisateur["prenoms"], utilisateur["email"],
                         utilisateur["contact"], utilisateur["age"], utilisateur["adresse"], utilisateur["type"],
                         utilisateur["sexe"], utilisateur["mdp"], utilisateur["localisation"])
        self._titre = titre
        self._profession = profession
        self._formations = formations
        self._experiences = experiences
        self._actes = actes
        self._presentation = presentation
        self._langues = langues

    @property
    def actes(self):
        return self._actes

    @actes.setter
    def actes(self, actes):
        self._actes = actes

    def to_json(self):
        dictionaire = {
            "utilisateur": {
                "id": super().id,
                "nom": super().nom,
                "prenoms": super().prenoms,
                "email": super().email,
                "contact": super().contact,
                "age": super().age,
                "adresse": super().adresse,
                "type": super().type,
                "sexe": super().sexe,
                "mdp": super().mdp,
                "localisation": super().localisation,
            },
            "titre": self._titre,
            "profession": self._profession,
            "formations": self._formations,
            "experiences": self._experiences,
            "presentation": self._presentation,
            "langues": self._langues,
            "actes": self._actes
        }

        return dictionaire
