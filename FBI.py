import pandas as pd
import matplotlib.pyplot as plt

# Chemin vers ton CSV
file_path = r"C:\Users\leurq\Downloads\Aggravated Assault Reported by Population_03-14-2026.csv"

# Lire le CSV
df_crime = pd.read_csv(file_path)

# Afficher les 10 premières lignes pour vérifier
print("Aperçu des données :")
print(df_crime.head(10))

# Convertir toutes les colonnes mensuelles en numérique, remplacer les erreurs par NaN
for col in df_crime.columns[1:]:
    df_crime[col] = pd.to_numeric(df_crime[col], errors='coerce')

# Transformer en format long
df_long = df_crime.melt(id_vars=['Series'],
                        var_name='Month',
                        value_name='Value')

# Convertir Month en datetime, ignorer les erreurs
df_long['Month'] = pd.to_datetime(df_long['Month'], format='%m-%Y', errors='coerce')

# Remplacer les NaN par 0 pour pouvoir tracer
df_long['Value'] = df_long['Value'].fillna(0)

# Supprimer les lignes où Month est NaT (problème de conversion)
df_long = df_long.dropna(subset=['Month'])

# Lister toutes les séries disponibles
print("\nSéries disponibles :")
print(df_long['Series'].unique())

# Tracer toutes les séries sur le même graphique
plt.figure(figsize=(14,7))
for series in df_long['Series'].unique():
    df_plot = df_long[df_long['Series'] == series]
    plt.plot(df_plot['Month'], df_plot['Value'], marker='o', label=series)

plt.title("Toutes les séries de criminalité (FBI)")
plt.xlabel("Date")
plt.ylabel("Nombre / taux")
plt.legend()
plt.grid(True)
plt.show()

