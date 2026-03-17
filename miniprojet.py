#1️⃣ Crée un DataFrame avec :

#nom

#salaire

#département

#2️Filtre les personnes avec un salaire > 3000
#3️Sauvegarde le résultat dans salaires_filtrés.csv

import pandas as pd

data ={



    "nom": ["Leboutte", "Sunny","Serron"],
    "salaire": [4500, 6300,5500],
    "departement": ["Finance", "HR", "Cadre"],
}
df = pd.DataFrame(data)
print (df)
df_filtre = df[df["salaire"]> 3000]
print (df_filtre)
df_filtre.to_csv ("resultat.csv", index=False)

