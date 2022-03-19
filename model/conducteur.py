from model.utilisateur import Utilisateur


class Conducteur(Utilisateur):
    def __init__(self,
                 numero_identifiant: int, nom_utilisateur: str,
                 mot_de_passe: str, sexe: str,
                 adresse_mail: str, nom: str,
                 prenom: str, telephone: str,
                 type_permis: str, annee_experience: int,
                 annee_obtention_permis: int,
                 age: int, profession: str):
        super(Conducteur, self).__init__(
            numero_identifiant, nom_utilisateur,
            mot_de_passe, sexe,
            adresse_mail, nom,
            prenom, telephone)
        self.type_permis = type_permis
        self.annee_experience = annee_experience
        self.age = age
        self.profession = profession
        self.annee_obtention_permis = annee_obtention_permis

    def __str__(self):
        return "[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
            self.numero_identifiant, self.nom_utilisateur,
            self.mot_de_passe, self.sexe,
            self.adresse_mail, self.nom,
            self.prenom, self.telephone,
            self.type_permis, self.annee_obtention_permis,
            self.annee_experience, self.age,
            self.profession)

