class Utilisateur:
    def __init__(self,
                 numero_identifiant: int, nom_utilisateur: str,
                 mot_de_passe: str, sexe: str,
                 adresse_mail: str, nom: str,
                 prenom: str, telephone: str):
        self.numero_identifiant = numero_identifiant
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.adresse_mail = adresse_mail
        self.sexe = sexe
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone

    def __str__(self):
        return "[{}, {}, {}, {}, {}, {}, {}]".format(
            self.numero_identifiant, self.nom_utilisateur,
            self.mot_de_passe, self.sexe,
            self.adresse_mail, self.nom,
            self.prenom, self.telephone)

