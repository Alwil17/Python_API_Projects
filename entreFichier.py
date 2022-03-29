from prime import Usage         # Du module prime.py importer la methode Usage
import os                       # Importer la bibliotheque os de python

for fichier in os.listdir("txt/"):      # Parcourir le repertoire nommé txt
    flic = open(os.path.join("txt/", fichier), 'r')         # ouvrir tous les fichiers du repertoire nommé txt en mode lecture
    with open(os.path.join("txt/", fichier), 'r') as flic:  # ouvrir tous les fichiers du repertoire nommé txt en mode lecture
        lecture = []            # Creation d'une liste vide
        for x in flic.readlines():          # Parcourir toutes les lignes de chacun des fichier ouvers dans la variable flic
            l = lecture.append(x.replace('\n',''))      # on remplace \n a la fin de chaque ligne par un caractere nul
    Usage(lecture)              # Appel de la methode Usage
              