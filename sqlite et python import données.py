import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seab_orn as sns

# 1️⃣ Créer la base SQLite et les tables avec les données
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

# Création des tables
cursor.executescript("""
DROP TABLE IF EXISTS utilisateurs;
DROP TABLE IF EXISTS commandes;

CREATE TABLE utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
);

CREATE TABLE commandes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur_id INTEGER,
    produit TEXT NOT NULL,
    prix REAL,
    date_commande TEXT,
    quantite INTEGER DEFAULT 1,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id)
);

-- Ajouter des utilisateurs
INSERT INTO utilisateurs (nom, email, age) VALUES 
('Alice', 'alice@example.com', 25),
('Bob', 'bob@example.com', 30),
('Charlie', 'charlie@example.com', 22),
('David', 'david@example.com', 28);

-- Ajouter des commandes (exemple)
INSERT INTO commandes (utilisateur_id, produit, prix, date_commande, quantite) VALUES
(1, 'ordinateur', 1000, '2026-03-01', 1),
(2, 'souris', 25, '2026-03-01', 1),
(1, 'clavier', 45.9, '2026-03-01', 1),
(4, 'écran', 200, '2026-03-01', 1),
(1, 'souris', 25, '2026-03-02', 1),
(3, 'webcam', 50, '2026-03-02', 1),
(1, 'ordinateur', 1000, '2026-03-03', 1),
(2, 'souris', 25, '2026-03-03', 1),
(1, 'clavier', 45.9, '2026-03-03', 1),
(4, 'écran', 200, '2026-03-03', 1);
""")

conn.commit()

# 2️⃣ Extract
df = pd.read_sql_query("SELECT * FROM commandes", conn)

# 3️⃣ Transform
df['quantite'] = df['quantite'].fillna(1)
df_grouped = df.groupby('utilisateur_id')['quantite'].sum().reset_index()
df_grouped['rang'] = df_grouped['quantite'].rank(method='dense', ascending=False).astype(int)

# Ajouter le nom des utilisateurs
df_users = pd.read_sql_query("SELECT id, nom FROM utilisateurs", conn)
df_grouped = df_grouped.merge(df_users, left_on='utilisateur_id', right_on='id')
df_grouped = df_grouped[['nom', 'quantite', 'rang']]

# 4️⃣ Load
df_grouped.to_csv('top_clients.csv', index=False)

conn.close()

# 5️⃣ Graphique
sns.barplot(data=df_grouped, x='nom', y='quantite', palette='viridis')
plt.title("Top Clients par Quantité Commandée")
plt.xlabel("Nom du Client")
plt.ylabel("Quantité Totale")
plt.show()

print("✅ Script terminé ! Le fichier 'top_clients.csv' et le graphique ont été générés.")
print(df_grouped)