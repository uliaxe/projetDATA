import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf  # Pour les graphiques en chandelles

# Générer des données factices
np.random.seed(42)  # Pour la reproductibilité
dates = pd.date_range(start="2023-01-01", periods=100, freq='B')  # 100 jours ouvrés
open_prices = np.random.uniform(100, 200, size=100)
high_prices = open_prices + np.random.uniform(1, 5, size=100)
low_prices = open_prices - np.random.uniform(1, 5, size=100)
close_prices = open_prices + np.random.uniform(-2, 2, size=100)
volumes = np.random.randint(100000, 1000000, size=100)

# Créer le DataFrame avec les données
data = pd.DataFrame({
    'date': dates,
    'ouv': open_prices,
    'haut': high_prices,
    'bas': low_prices,
    'clot': close_prices,
    'vol': volumes
})

# Renommer les colonnes pour qu'elles correspondent aux noms attendus par mplfinance
data.rename(columns={
    'ouv': 'Open',
    'haut': 'High',
    'bas': 'Low',
    'clot': 'Close',
    'vol': 'Volume'
}, inplace=True)

# Calcul de l'écart-type des prix de clôture
volatilite = data['Close'].std()
print(f"\nÉcart-type des prix de clôture : {volatilite:.2f}")

# Visualisation des chandelles (Graphique)
data.set_index('date', inplace=True)  # Mettre la date en index
mpf.plot(data, type='candle', style='charles', title="Graphique en chandelles", ylabel='Prix', volume=True)

# Affichage des statistiques descriptives des prix de clôture
print("\nStatistiques descriptives des prix de clôture :")
print(data['Close'].describe())

# Visualisation de l'écart-type des prix de clôture
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label="Prix de clôture")
plt.axhline(y=data['Close'].mean(), color='r', linestyle='--', label='Moyenne')
plt.axhline(y=data['Close'].mean() + volatilite, color='g', linestyle='--', label='Moyenne + Écart-type')
plt.axhline(y=data['Close'].mean() - volatilite, color='g', linestyle='--', label='Moyenne - Écart-type')
plt.title('Prix de clôture avec écart-type')
plt.xlabel('Date')
plt.ylabel('Prix')
plt.legend()
plt.grid(True)
plt.show()
