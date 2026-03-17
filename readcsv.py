
#creer un csv
import pandas as pd
data={
    "employee": ["Alice", "Bob", "Clara", "David", "Emma"],
     "salaire": [ 3000,4500,3500,5000,2800],
     "departement": ["HR","Finance","HR","Finance","HR"],
 }
df = pd.DataFrame(data)
df.to_csv ("employee.csv", index=False) #sauvgarde csv
#lire le csv dans un DataFrame
df = pd.read_csv("employee.csv")
print("DataFrame lu depuis le csv:")
print(df)
 #Filtrer , calculer et sauvgarder

df_filtre = df [df["salaire"]>3000]

 #calcul du salaire  moyen et total par departement

stat_salaire = df.groupby("departement")["salaire"].agg(
     salaire_moyen= "mean",
     salaire_total="sum"
 )
#sauvgarder les resultats filtres
df_filtre.to_csv ("resultat_filtre.csv", index=False)
print("\nEmployee filtres  :")
print (df_filtre)

print("\nStatistiques par departement :")
print (stat_salaire)



print