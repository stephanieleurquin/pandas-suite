import pandas as pd
import matplotlib.pyplot as plt

# Chemin exact vers ton CSV
file_path = r"C:\Users\leurq\Downloads\Aggravated Assault Reported by Population_03-14-2026.csv"

# 1️⃣ Lire le CSV
df_crime = pd.read_csv(file_path)

# 2️⃣ Convertir toutes les colonnes mensuelles en numérique
for col in df_crime.columns[1:]:
    df_crime[col] = pd.to_numeric(df_crime[col], errors='coerce')

# 3️⃣ Transformer le CSV en format long
df_long = df_crime.melt(id_vars=['Series'],
                        var_name='Month',
                        value_name='Value')

# 4️⃣ Convertir Month en datetime
df_long['Month'] = pd.to_datetime(df_long['Month'], format='%m-%Y', errors='coerce')

# 5️⃣ Supprimer les lignes où Month ou Value sont NaN
df_long = df_long.dropna(subset=['Month', 'Value'])

# 6️⃣ Filtrer uniquement les années complètes 2021-2025
df_long = df_long[(df_long['Month'].dt.year >= 2021) & (df_long['Month'].dt.year <= 2025)]

# 7️⃣ Créer le graphique pour toutes les séries disponibles
plt.figure(figsize=(14,7))
for series in df_long['Series'].unique():
    df_plot = df_long[df_long['Series'] == series]
    plt.plot(df_plot['Month'], df_plot['Value'], marker='o', label=series)

plt.title("Crimes aux USA (FBI) 2021-2025")
plt.xlabel("Date")
plt.ylabel("Nombre d'incidents")
plt.legend()
plt.grid(True)
plt.show()
