from model.utilisateur import Utilisateur


class Client(Utilisateur):
    def __init__(self,
                 numero_identifiant: int, nom_utilisateur: str,
                 mot_de_passe: str, sexe: str,
                 adresse_mail: str, nom: str,
                 prenom: str, telephone: str,
                 situation_matrimoniale: str, profession: str,
                 nombre_enfants: int = 0
                 ):
        super(Client, self).__init__(numero_identifiant, nom_utilisateur,
                                     mot_de_passe, sexe,
                                     adresse_mail, nom,
                                     prenom, telephone)
        self.situation_matrimoniale = situation_matrimoniale
        self.profession = profession
        self.nombre_enfants = nombre_enfants

    def __str__(self):
        return "[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
            self.numero_identifiant, self.nom_utilisateur,
            self.mot_de_passe, self.sexe,
            self.adresse_mail, self.nom,
            self.prenom, self.telephone,
            self.situation_matrimoniale, self.profession,
            self.nombre_enfants)
