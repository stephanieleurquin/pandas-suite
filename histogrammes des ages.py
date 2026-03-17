import pandas as pd
import matplotlib.pyplot as plt

# Données
data = {"prenom": ["Sophie", "Anne", "Michele", "Gilles", "Sophie", "Anne"],
        "age": [25, 30, 22, 35, 25, 30]}
df = pd.DataFrame(data)

counts = df['prenom'].value_counts()
ages = df["age"]

# Créer une figure avec 3 sous-graphes
fig, axs = plt.subplots(1, 3, figsize=(18,5))  # 1 ligne, 3 colonnes

# 1️⃣ Diagramme en barres
axs[0].bar(counts.index, counts.values, color='lightgreen')
axs[0].set_title("Nombre de personnes par prénom")

# 2️⃣ Camembert
axs[1].pie(counts.values, labels=counts.index, autopct='%1.1f%%')
axs[1].set_title("Répartition des prénoms")

# 3️⃣ Histogramme des âges
axs[2].hist(ages, bins=5, color='skyblue', edgecolor='black')
axs[2].set_title("Histogramme des âges")
axs[2].set_xlabel("Âge")
axs[2].set_ylabel("Nombre de personnes")

plt.tight_layout()  # ajuste l'espacement
plt.show()          # tout s'affiche dans **une seule fenêtre**