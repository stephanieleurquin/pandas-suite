
import pandas as pd

df = pd.DataFrame({
    "nom": ["Alice", None, "Bob"],
    "age": [25, None, 30]
})

print("Avant fillna :")
print(df)

# remplacer les NaN par "inconnu" pour le nom et 0 pour l'âge
df["nom"] = df["nom"].fillna("inconnu")
df["age"] = df["age"].fillna(0)

print("\nAprès fillna :")
print(df)