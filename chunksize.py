import pandas as pd

# 1. Créer les données
data = {
    "employee": ["Alice", "Bob", "Clara", "David", "Emma",
                 "Frank", "Grace", "Henry", "Irene", "John"],
    "salaire": [3000, 4500, 5000, 2800, 3200, 4000, 2900, 3600, 4200, 3100],
    "departement": ["HR", "Finance", "HR", "Finance", "HR", "IT", "IT", "Finance", "HR", "IT"]
}

# 2. Créer le CSV
df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)
print("CSV créé avec succès !")

# 3. Lire le CSV
df = pd.read_csv("employees.csv")
print("\nContenu du CSV :")
print(df)

# 4. Filtrer les employés avec salaire > 3000
df_filtre = df[df["salaire"] > 3000]

# 5. Calcul du salaire moyen et total par département
stat_salaire = df.groupby("departement")["salaire"].agg(
    salaire_moyen="mean",
    salaire_total="sum"
)

# 6. Sauvegarder les résultats filtrés
df_filtre.to_csv("resultat_filtre.csv", index=False)

# 7. Afficher les résultats filtrés
print("\nEmployés filtrés (salaire > 3000) :")
print(df_filtre)

# 8. Afficher les statistiques par département
print("\nStatistiques par département :")
print(stat_salaire)

# 9. Lecture du CSV par morceaux (chunksize = 2)
print("\nLecture du CSV par morceau (chunksize=2) :")
chunksize = 2
for chunk in pd.read_csv("employees.csv", chunksize=chunksize):
    print(chunk)
