#Exercice 1 — Filtrage simple

#Objectif : filtrer des données selon une condition.

#Crée un DataFrame avec ces données :

#nom	age	ville
#Alice	24	Paris
#Bob	32	Lyon
#Clara	29	Marseille
#David	35	Paris

#Filtre les personnes dont l’âge est supérieur à 30.

#Affiche le résultat.

import pandas as pd

data = {
   "nom" :["Alice", "Bob", "Clara", "David"], #attention au guilllemnt poiur les noms
    "age": [ 55, 28,61,33],
    "ville": ["Paris", "Lyon", "Marseille"],



}

df_filtre =df[df["age"] > 30],
print (df_filtre)
