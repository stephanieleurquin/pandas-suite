# novus_interpreteur.py

# Dictionnaire pour stocker les variables
variables = {}

def executer_ligne(ligne):
    ligne = ligne.strip()  # enlève les espaces inutiles

    # ignorer les lignes vides ou les commentaires
    if ligne == "" or ligne.startswith("#"):
        return

    mots = ligne.split()

    # Commande "dire"
    if mots[0] == "dire":
        try:
            texte = ligne.split('"')[1]  # récupère le texte entre guillemets
            print(texte)
        except IndexError:
            print("Erreur : syntaxe correcte → dire \"texte\"")

    # Commande "set" pour créer une variable
    elif mots[0] == "set":
        if len(mots) < 3:
            print("Erreur : syntaxe correcte → set nom_variable valeur")
            return
        nom_var = mots[1]
        try:
            valeur = int(mots[2])
        except ValueError:
            print("Erreur : la valeur doit être un nombre")
            return
        variables[nom_var] = valeur
        print(f"Variable {nom_var} créée avec la valeur {valeur}")

    # Commande "addition"
    elif mots[0] == "addition":
        if len(mots) < 3:
            print("Erreur : syntaxe correcte → addition nombre1 nombre2")
            return
        def valeur_ou_var(mot):
            if mot in variables:
                return variables[mot]
            try:
                return int(mot)
            except ValueError:
                print(f"Erreur : {mot} n'est pas une variable ou un nombre")
                return None
        a = valeur_ou_var(mots[1])
print("Bienvenue dans Novus ! Tape 'exit' pour quitter.")

while True:
    ligne = input("Novus> ")
    if ligne.lower() in ["exit", "quit"]:
        break
    executer_ligne(ligne)
