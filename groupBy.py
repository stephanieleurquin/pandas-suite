#Étapes à suivre

#1️⃣ Créer le DataFrame
#2️⃣ Calculer le salaire moyen par département avec groupby().mean()
#3️⃣ Calculer le salaire total par département avec groupby().sum()



import pandas as pd

data= {
    "employe":["Alice","Bob","Clara","David"],
    "salaire" : [3000,4500,3500,5000],
    "departement": ["HR", "Finance", "HR", "Finance"],
}
df= pd.DataFrame(data)
print("Dataframe complet: ")
print (df)
#Calculer  le salaire moyen par departement
salaire_moyen =df.groupby("departement")["salaire"].mean()
print ("\nsalaire_moyen : ", salaire_moyen)


# calculer le salaire total par departement

total_salaire =df.groupby("departement")["salaire"].sum()
print ("total salaire_moyen: ",total_salaire)