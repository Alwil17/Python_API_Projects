class Specialite:

    def __init__(self,id:int = 0,nom:str = "Test"):
        self.id = id
        self.__nom = nom
        
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    def to_json(self):
        dictionaire = {
            "id": self.id,
            "nom": self.__nom,
        }

        return dictionaire