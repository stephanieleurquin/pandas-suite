import pandas as pd
#---lire 1 le CSV---
df = pd.read_csv(r"C:\Users\leurq\Desktop\ventes.csv")

#--2 nettoyer les colonnes--
#supprimer  les lignes avec les valeurs manquantes
df = df.dropna()

#3 Ajouter une colonne'total'--
df["Total"] = df["Prix"] * df ["Quantite"]

#4 sauvgarder dans un nouveau csv---
df.to_csv(r"C:\Users\leurq\Desktop\ventes_clean.csv", index=False)

print ("pipeline ETL termine. fichier'ventes_clean.csv'créé!")
