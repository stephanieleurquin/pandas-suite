# pipeline_finance.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# 1️⃣ Récupérer les données financières
ticker = "AAPL"  # Exemple : Apple
data = yf.Ticker(ticker)
import sqlalchemy
print(sqlalchemy.__version__)



# Historique sur 1 mois
df = data.history(period="1mo")

# 2️⃣ Réinitialiser l'index pour avoir la date comme colonne normale
df = df.reset_index()

# 3️⃣ Vérifier les colonnes et types
print("Colonnes disponibles :", df.columns)
print(df.dtypes)

# 4️⃣ Calculer la variation en pourcentage du prix de clôture
df['Variation'] = df['Close'].pct_change() * 100  # en pourcentage

# 5️⃣ Afficher les 5 premières lignes
print(df[['Date','Open','High','Low','Close','Volume','Variation']].head())

# 6️⃣ Afficher un graphique du prix de clôture
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], marker='o')
plt.title(f"Prix de clôture de {ticker} sur 1 mois")
plt.xlabel("Date")
plt.ylabel("Prix de clôture ($)")
plt.grid(True)
plt.show()

# 7️⃣ Stocker les données dans une base SQLite locale
engine = create_engine('sqlite:///finance.db')
df.to_sql('AAPL_prices', engine, if_exists='replace', index=False)
print("Données stockées dans finance.db -> table AAPL_prices")

