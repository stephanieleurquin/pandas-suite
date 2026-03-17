#lancer  un des à 6 faces
# 1 declarer tous les resultats possibles
#tous les resultats possible quand on lance le des
S= [1,2,3,4,5,6]

#etape 2 :definir l evenement
E = [x for x in S if x > 4] #les resultas seront superieurs à 4 (5,6)

#3 calculer la probabilite
#probabilite= nombre de cas favorables / nombre total de cas
P = len(E) / len(S) #len E , nombre de cas favorable et len S nombre total de cas

#afficher les resultat

print ("resultats possible : ", S)
print ("evenement : " ,E)
print("probabilite : ",P)
