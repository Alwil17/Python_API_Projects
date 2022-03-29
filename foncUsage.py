import json


def Usage():                    # Déclaration de la Methode Usage
    global tab, j, i, pEss      # Déclaration des variables tab, j, i, pEss avec une encapsulation de type global
    # i parcour nombre de places \ j parcour la puissance en Essence
    # tab enregistre le tableau correspondant a notre USAGE
    # pEss correspond a la puissance finale qui parcourera le tableau

    with open('USAGE.json', 'r') as f:      # Ouvrir le fichier USAGE.json
        matrice = json.load(f)              # matrice prend toutes les donnees dans USAGE.json
  
    print("Types d'usage !!! ")
    print("\n1- Promenade et Affaires (PA) ")
    print("\n2- Transport pour son Propre Compte (TPC) ")
    print("\n3- Taxi ")
    print("\n4- Tramsport Public Voyageurs (TPV) ")
    print("\n5- Transport Public Marchandises (TPM) ")

    # usage prend le choix du type d'usage du vehicule a assurer
    usage = int(input("\nEntrez le choix svp : "))
    while usage<1 or usage>5 :          # Controle sur la plage reservée au choix du type d'usage du vehicule
        usage = int(input("\nEntrez le choix svp (entre 1, 2, 3, 4 et 5) : "))

    nb = int(input("\n\nEntrez le nombre de place : "))     # nb prend en compte le nombre de place du Vehicule

    # tab ici prendra le tableau specifique ( referencé dans le fichier USAGE.json ) de l'usage choisi plus haut
    # CP est le coup de piece du vehicule. Il varie en fonction du type d'usage
    # GPT Taxe liée au type d'usage du vehicule et du nombre de places (ne prend que deux valeurs possibles 1000 ou 1500 )
    
    if usage == 1:
        tab = matrice["PA"]
        strUsage = "Promenade Affaire"
        while nb<5 or nb>15:            # Controle sur la plage reservée au choix du nombre de places d'un vehicule de type PA (Promenade et affaires)
            nb = int(input("\n\nEntrez le nombre de place (Entre [5;15]) : "))

        # imax = 10
        CP = 5000
        GPT = 1500*nb
        if nb == 5:
            j = 0
        elif nb == 6:
            j = 1
        elif nb == 7:
            j = 2
        elif nb == 8:
            j = 3
        elif nb == 9:
            j = 4
        elif nb == 10:
            j = 5
        elif nb == 11:
            j = 6
        elif nb == 12:
            j = 7
        elif nb == 13:
            j = 8
        elif nb == 14:
            j = 9
        elif nb == 15:
            j = 10

    elif usage == 2:
        tab = matrice["TPC"]
        strUsage = "Transport pour son Propre Compte"
        while nb<2 or nb>4 and nb!=6:           # Controle sur la plage reservée au choix du nombre de places d'un vehicule de type TPC (Transport pour son Propre Compte)     
            nb = int(input("\n\nEntrez le nombre de place (Entre 2, 3, 4 et 6) : "))

        # imax = 3
        CP = 5000
        GPT = 1500 * nb
        if nb == 2:
            j = 0
        elif nb == 3:
            j = 1
        elif nb == 4:
            j = 2
        elif nb == 6:
            j = 3

    elif usage == 3:
        tab = matrice["TAXI"]
        strUsage = "Taxi"
        while nb!=5 and nb!=6 and nb!=8 and nb!=9 and nb!=10:       # Controle sur la plage reservée au choix du nombre de places d'un vehicule de type Taxi
            nb = int(input("\n\nEntrez le nombre de place (Entre 5, 6, 8, 9 et 10) : "))

        # imax = 4
        CP = 10000
        GPT = 1500
        if nb == 5:
            j = 0
        elif nb == 6:
            j = 1
        elif nb == 8:
            j = 2
        elif nb == 9:
            j = 3
        elif nb >= 10:
            j = 4

    elif usage == 4:
        tab = matrice["TPV"]
        strUsage = "Transport Public Voyageurs"
        while nb<12:
            nb = int(input("\n\nEntrez le nombre de place (superieur ou egale a 12 places) : "))
        # imax=1
        CP = 10000
        GPT = 1500
        if nb >= 12 & nb <= 15:
            j = 0
        elif nb >= 16:
            j = 1

    elif usage == 5:
        tab = matrice["TPM"]
        strUsage = "Transport Public Marchandises"
        while nb<2 or nb>4:
            nb = int(input("\n\nEntrez le nombre de place (Entre 2, 3 et 4) : "))
        # imax=2
        CP = 10000
        GPT = 1500
        if nb == 2:
            j = 0
        elif nb == 3:
            j = 1
        elif nb == 4:
            j = 2

    # pprint.pprint(tab)
    print("\nType de carburant !!!!\n")
    print("\n1. Essence")
    print("\n2. Diesel")

    # carbu prend le choix du type de carburant
    carbu = int(input("\nEntrez votre choix : "))
    #faire des exceptions
    while carbu!=1 and carbu!=2:  #"a"<=carbu<="z" or "A"<=carbu<="Z" or
        carbu = int(input("\nEntrez votre choix (entre 1 et 2) : "))

    # pu prend en paramettre la puissance brute tout carburant confondu(Essence comme Diesel)
    pu = int(input("\n\nEntrez la puissance du vehicule : "))

    # pEss est la valeur final en essence qui parcourra les differents tableaux
    if carbu == 2:  # Si le carburant est Diesel, Convertion
        strPu = "Diesel"
        if pu == 1:
            pEss = 1
        elif pu == 2:
            pEss = 3
        elif pu == 3:
            pEss = 4
        elif pu == 4:
            pEss = 6
        elif pu == 5:
            pEss = 7
        elif pu == 6:
            pEss = 9
        elif pu == 7:
            pEss = 10
        elif pu == 8:
            pEss = 11
        elif pu == 9:
            pEss = 13
        elif pu == 10:
            pEss = 14
        elif pu == 11:
            pEss = 16
        elif pu == 12:
            pEss = 17
        elif pu == 13:
            pEss = 19
        elif pu == 14:
            pEss = 20
        elif pu == 15:
            pEss = 21
        elif pu == 16:
            pEss = 23
        elif pu >= 17:
            pEss = 24
    elif carbu == 1:  # Si carburant est Essence pas de conversion
        strPu = "Essence"
        pEss = pu

    if pEss <= 2:
        i = 0
    if 3 <= pEss <= 6:
        i = 1
    if 7 <= pEss <= 10:
        i = 2
    if 11 <= pEss <= 14:
        i = 3
    if 15 <= pEss <= 23:
        i = 4
    if pEss >= 24:
        i = 5



    PB = tab[i][j] # PB est le prix de base
    Prime = PB + CP + ((6/100)*(PB+CP)) + GPT  # Prime c'est la prime finale que doit payer l'assuré a l'assurance
    print("\nla Prime finale du vehicule est : {:.2f}".format(Prime))

    fichier = open("result_fUsage.json","a")
    #fichier.write("La valeur de base est " + str(tab[i][j]) + "\n")
    fichier.write("La Prime finale du vehicule de type " + strUsage + ", de type de carburant " + strPu + " et de puissance " + str(pu) + "cv est " + str(Prime) + "\n")


Usage()
