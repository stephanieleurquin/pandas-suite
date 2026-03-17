import pandas as pd

# lire le csv existant
df= pd.read_csv ("employees.csv")

#calculer le salaire moyen et total par departement
stat = df.groupby("departement")["salaire"].agg( #departement n,e st aps aligne  comme els autres , parcequ il devient l index du DataFrame

    salaire_moyen="mean",
    salaire_total="sum"

)
#afficher les resultats
print ("statistique par departement")
print (stat)
#sauvgarder dans un nouveau CSV
stat.to_csv("stat_departement.csv",index=True)
print ("\nLes startistiques ont été sauvgardées dans stat_departement.csv")