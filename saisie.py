def saisir():
    nb=-2

    while nb <0:
        print("***************Calculer une table***************")
        nb = input("Bonjour, veuillez saisir une valuer numérqiue positive : ")
        print(" ")
        
        try:
            nb = int(nb)
        except:
            print("Vous n'avez pas saisie une valeur numérique positif")
            
            
        else:
            print(f"***************Table de {nb}***************")
        return nb
    