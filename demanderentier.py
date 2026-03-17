#demander un entier à l utilisateur
while True:
    try:
        nombre = int(input("donnes -moi un nombre entier "))
        if  nombre >0:
            break
        else:
            print("ca doit etre un nombre ")
    except ValueError:
        print("le nombre  doit etre un chiffre")

