prenoms= ["Sophie","Anne", "Michele"," Gilles", "Claudine", "Tom","Lina" , "Sophie", "Anne","Gilles"]
compteur={}
for prenom in prenoms:
    if prenom in compteur:
        compteur[prenom]=compteur[prenom]+1

    else :
        compteur [prenom] = 1

for prenom , nombre in compteur.items():
            print(prenom,";", nombre)