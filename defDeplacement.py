def foret():
    print("t'es dans la foret")
    return(foret)

def lac():
    print("t'es au lac")
    return(lac)


def montagnes():
    print("t'es dans les montagnes")
    return(montagnes)

def village():
    print("t'es au village")
    deplacementVillage= str(input("veux tu aller vers: la forge ou la bibliotheque ?         "))
    verification = False
    while verification == False:  
        if deplacementVillage == "forge" or deplacementVillage == "bibliotheque" :
            if deplacementVillage == "forge":
                zone = "forge"
                forge()
                verification = True
            elif deplacementVillage== "bibliotheque":
                zone = "bibliotheque"
                bibliotheque()
                verification = True
        else:
            print("je n'ai pas compris veux tu aller dans la forge ou la bibliotheque")     
    return(village)

def forge():
    print("t'es dans la forge")
    return(forge)

def bibliotheque():
    print("t'es dans la bibliotheque")
    return(bibliotheque)

def grotte():
    print("t'es dans la grotte")
    return(grotte)