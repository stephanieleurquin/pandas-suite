#Créer un DataFrame avec des employés, leur salaire et leur département

#Filtrer les employés avec un salaire > 3000

#Calculer le salaire moyen et le salaire total par département

#Sauvegarder les résultats filtrés dans un CSV


import pandas as pd
#creer  un Data Frame avec des employee , leur salaire et leur departement

data= {
    "employees": [" Alice", "Bob", "Clara", "David", "Emma"],
    "salaire" : [ 3000, 4500,3500,5000,2800],
    "departement":["HR","Finance","HR","Finance","HR"],
}
df= pd.DataFrame(data)
print("DataFrame complet: ")
print (df)
 #filtrer  les employes  avec un salaire >3000
df_filtre=df[df ["salaire"] > 3000]
print (df_filtre)
df_filtre.to_csv ( "resultat.csv", index= False)
#Calculer  le salaire moyen par departement
salaire_moyen =df.groupby ("departement") ["salaire"].mean()
print ("\nsalaire_moyen : ", salaire_moyen)

#calculer le salaire moyen et le salaire total
salaire_moyen =df.groupby("departement") ["salaire"].sum()
print ("totalsalaire_moyen : ", salaire_moyen)