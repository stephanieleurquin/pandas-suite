#demander plusieurs prenoms  et dire quel est le plus long
prenom1 =(input ("Quel est ton prenom ?"))
prenom2 = (input ("quel est ton prenom ?"))
prenom3 = (input ("quel est ton prenom ?"))
prenom4 = (input ("quel est ton prenom ?"))
prenom5 = (input ("quel est ton prenom ?"))
#utiliser une liste pour stocker plusieurs valeurs
prenom = [prenom1,prenom2,prenom3, prenom4,prenom5]
len (prenom)
prenom_le_plus_long = max (prenom , key=len)


#afficher le resultat
print ("le prenom le plus long est :", prenom_le_plus_long)



