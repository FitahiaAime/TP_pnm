def menu_afficher():
    print("MENU DU BOISSONS")
    print("1.APPRENDRE DU THE")
    print("2.APPRENDRE DU EAU")
    print("3.APPRENDRE DU JUS")
    print("4.quiter")
    
def demander_choix():
    return input("QUE SOUHAITEZ-VOUS : ")

while True :
    menu_afficher()
    choix = demander_choix()
    
    if choix == "1":
        print("vouz avez choisis thé")
    elif choix == "2" :
        print("vous avez choisiz eau")
    elif choix == "3":
        print("vous avez choix jus.")
        
        break
    else :
        print("merci! au revoir")
    

    