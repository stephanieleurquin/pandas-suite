from collections import Counter
prenoms= ["Sophie","Anne","Michele","Gilles", "Claudine", "Tom", "Lina", "Sophie", "Anne", "Gilles"] #attention ne pas oublier = 
#compteur automatique
compteur = Counter(prenoms)
#affichage
for prenom, nombre in compteur.items():
    print (prenom, ";",nombre)
