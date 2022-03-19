class Etablissement:
    def __init__(self, id: int, nom: str, email: str, adresse: str, contact: str, actes):
        self.__id = id
        self.__nom = nom
        self.__email = email
        self.__adresse = adresse
        self.__contact = contact
        self.__actes = actes

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self, adresse):
        self.__adresse = adresse

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact):
        self.__contact = contact

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact):
        self.__contact = contact

    @property
    def actes(self):
        return self.__actes

    @actes.setter
    def actes(self, actes):
        self.__actes = actes

    def to_json(self):
        dictionnaire = {
            "id": self.__id,
            "nom": self.__nom,
            "email": self.__email,
            "adresse": self.__adresse,
            "contact": self.__contact,
            "actes": self.__actes
        }
        return dictionnaire
