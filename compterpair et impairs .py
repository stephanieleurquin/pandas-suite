# compter pair et impair dans une liste
nombre= [5,9,7,12,24]
#initialiser les compteur
compteur_pair= 0
compteur_impair= 0
#parcourir la liste
for n in nombre:
    if n % 2 == 0:
        compteur_pair +=1
    else:
        compteur_impair += 1
#compter combien de nombre sont pair ou impairs
#afficher les resultats
print("pairs :", compteur_pair)
print("impairs :", compteur_impair)