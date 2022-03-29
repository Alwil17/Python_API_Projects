import json

from controllers.utilisateur_controller import get_user_by_email


class Auth:
    connected_user = {}

    def __init__(self, email: str = "", password: str = "") -> None:
        self.email = email
        self.password = password
        self.firstAction()

    def showLoginForm(self, errors: bool = False, error_message: str = ""):
        print('---------- Connexion ----------')
        if (errors):
            print(error_message)
        self.email = input("Email: ")
        self.password = input("Mot de passe: ")
        self.connecter(self.email, self.password)

    def connecter(self, email, password):
        valid_user = False
        with open('database.json', 'r') as file:
            base_de_donnees = json.load(file)
            for user in base_de_donnees['utilisateurs']:
                if user["email"] == email and user["mdp"] == password:
                    valid_user = True
        if valid_user:
            Auth.connected_user = get_user_by_email(email)
            print('connecter avec succès')
        else:
            self.showLoginForm(True, "Ces identifiants ne figurent pas dans notre base de données !!!")

    def firstAction(self):
        print("Bienvenue dans RDV Medical")
        choix = int(input("1- Se connecter\n 2- S'inscrire"))
        while choix != 1 and choix != 2:
            choix = int(input("1- Se connecter\n 2- S'inscrire"))
        if (choix == 1):
            self.showLoginForm()
        elif (choix == 2):
            print("something")
        else:
            self.showLoginForm()
