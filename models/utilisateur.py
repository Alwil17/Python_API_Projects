class Utilisateur:
    def __init__(self, id: int, nom: str, prenoms: str, email: str, contact: str, age: int, adresse: str, sexe: str,
                 type: str, mdp: str, localisation):
        self._id = id
        self._nom = nom
        self._prenoms = prenoms
        self._email = email
        self._contact = contact
        self._age = age
        self._adresse = adresse
        self._sexe = sexe
        self._type = type
        self._mdp = mdp
        self._localisation = localisation

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def prenoms(self):
        return self._prenoms

    @prenoms.setter
    def prenoms(self, prenoms):
        self._prenoms = prenoms

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, adresse):
        self._adresse = adresse

    @property
    def sexe(self):
        return self._sexe

    @sexe.setter
    def sexe(self, sexe):
        self._sexe = sexe

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def mdp(self):
        return self._mdp

    @mdp.setter
    def mdp(self, mdp):
        self._mdp = mdp

    @property
    def localisation(self):
        return self._localisation

    @localisation.setter
    def localisation(self, localisation):
        self._localisation = localisation

    def to_json(self):
        dictionaire = {
            "id": self._id,
            "nom": self._nom,
            "prenoms": self._prenoms,
            "email": self._email,
            "contact": self._contact,
            "age": self._age,
            "adresse": self._adresse,
            "type": self._type,
            "sexe": self._sexe,
            "mdp": self._mdp,
            "localisation": self._localisation,
        }

        return dictionaire
