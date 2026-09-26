import string,time,random
mdp_gen = ""
param = {
    "all" : string.ascii_lowercase + string.digits+string.ascii_uppercase + string.punctuation,
    "taille" : 8,
    "majuscule": True,
    "special": True,
    "nombre" : True
}

while True:
    
    print("Parmetres du mot de passe :")
    print("Taille : ", param["taille"])
    print("Majuscules : ", param["majuscule"])
    print("Caracteres speciaux : ", param["special"])
    print("Caracteres numeriques : ", param["nombre"])
    print("------------------------------")
    print("1.Changer Les parametres")
    print("2.Generer le mot de passe")
    print("3.Quitter")
    choix = input("Choix : ")
    if choix not in ["1", "2", "3"]:
        print("Choix invalide")
        continue
        time.sleep(1)
    if choix == "1":
        while True:
            print("1.Changer la taille du mot de passe")
            print("2.Activer/Désactiver les majuscules")
            print("3.Activer/Désactiver les caracteres speciaux")
            print("4.Activer/Désactiver les caracteres numeriques")
            print("5.Retour")
            choix_param = input("Choix : ")
            if choix_param not in ["1", "2", "3", "4"]:
                print("Choix invalide")
                continue
                time.sleep(1)
            if choix_param == "1":
                param["taille"] = input("Nouvelle taille : ")
                while not param["taille"].isdigit() or int(param["taille"]) < 1:
                    print("Taille invalide")
                    param["taille"] = input("Nouvelle taille : ")
                param["taille"] = int(param["taille"])
                if param["taille"] < 8:
                    print(f"Attention : Un mot de passe de {param['taille']} caracteres est faible")
            elif choix_param == "2":
                param["majuscule"] = not param["majuscule"]
                if param["majuscule"]:
                    param["all"] += string.ascii_uppercase
                else:
                    param["all"] = param["all"].replace(string.ascii_uppercase, "")
                print("Majuscules : ", param["majuscule"])
            elif choix_param == "3":
                param["special"] = not param["special"]
                if param["special"]:
                    param["all"] += string.punctuation
                else:
                    param["all"] = param["all"].replace(string.punctuation, "")
                print("Caracteres speciaux : ", param["special"])
            elif choix_param == "4":
                param["nombre"] = not param["nombre"]
                if param["nombre"]:
                    param["all"] += string.digits
                else:
                    param["all"] = param["all"].replace(string.digits, "")
                print("Caracteres numeriques : ", param["nombre"])
            elif choix_param == "5":
                break
    elif choix == "2":
        for i in range(param["taille"]):
            mdp_gen += random.choice(param["all"])
        print("Mot de passe genere : ", mdp_gen)
    elif choix == "3":
        break

