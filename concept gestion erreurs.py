# demander un nombre à l'utilisateur et gérer les erreurs
while True:
    try:
        nombre = int(input("Donnes-moi un nombre positif : "))
        if nombre > 0:
            break  # nombre correct, on sort de la boucle
        else:
            print("Le nombre doit être positif, ressaye !")
    except ValueError:
        print("Ce n'est pas un nombre entier, ressaye encore !")

