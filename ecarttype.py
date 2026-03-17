import math # neccessaire pour la fonction sqrt
notes = [12,15,18,10,14,17,9]

# 1 creer une fonction
def calcul_stats ( notes)
    #calculer la moyenne
moyenne =sum(notes) / len (notes)
#trouver la note la plus haute
notes_max =max(notes)
#trouver la notes la plus faible
notes_min =min (notes)
#calculer l'ecart type
variance = summ((x -moyenne )**2 for x in notes) / len(notes)
ecart_type =math.sqrt(variance)
#retourner les resultats
return moyenne, note_max, note_min, ecart_type

#appeler la fonction
moyenne,notes_max,note_min, ecart=type =calcul_stats(notes)
#afficher resultats
print ("moyenne :", round(moyenne,2))
print ("note max :", notes_max)
print ("note min :", note_min)
print ("ecart-type :", round(ecart_type,2))
