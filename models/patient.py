from utilisateur import Utilisateur

class Patient(Utilisateur):
    def __init__ (self,id:int,nom:str,prenoms:str,email:str,contact:str,age:int,adresse:str,sexe:str,mdp:str):
        super().__init__(id,nom,prenoms,email,contact,age,adresse,sexe,mdp)