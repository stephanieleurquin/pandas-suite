import sqlite3
import pandas as pd

# 1️⃣ Connexion à la base SQLite
conn = sqlite3.connect('exercice.db')
cursor = conn.cursor()

# 2️⃣ Créer la table commandes si elle n'existe pas
cursor.execute("""
CREATE TABLE IF NOT EXISTS commandes (
    id INTEGER PRIMARY KEY,
    client_id INTEGER,
    produit TEXT
)
""")
conn.commit()

# 3️⃣ Ajouter des données d'exemple (si pas déjà présentes)
cursor.executemany("""
INSERT INTO commandes (client_id, produit) VALUES (?, ?)
""", [
    (1,'ordinateur'),
    (2,'souris'),
    (1,'clavier'),
    (4,'écran'),
    (1,'souris'),
    (3,'webcam')
])
conn.commit()

# 4️⃣ Lire la table dans un DataFrame Pandas
commandes = pd.read_sql("SELECT * FROM commandes", conn)
print(commandes)

# 5️⃣ Compter le nombre de commandes par client et ajouter un rang (simule ROW_NUMBER)
nb_commandes = commandes.groupby('client_id').size().reset_index(name='nb_commandes')
nb_commandes['rang'] = nb_commandes['nb_commandes'].rank(method='first', ascending=False).astype(int)

print(nb_commandes)

# 6️⃣ Fermer la connexion
conn.close()

