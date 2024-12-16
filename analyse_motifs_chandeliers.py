import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

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
    'Open': open_prices,
    'High': high_prices,
    'Low': low_prices,
    'Close': close_prices,
    'Volume': volumes
})

# Conversion de la colonne 'date' en DatetimeIndex et mise à jour de l'index
data['date'] = pd.to_datetime(data['date'], errors='coerce')
data.set_index('date', inplace=True)

# Vérification du type d'index
print(data.index)

# Fonction pour identifier l'étoile du matin
def is_morning_star(data, i):
    if i < 2:
        return False
    # Conditions pour l'étoile du matin
    first_candle = data['Close'].iloc[i-2] < data['Open'].iloc[i-2]  # Première bougie baissière
    second_candle = abs(data['Close'].iloc[i-1] - data['Open'].iloc[i-1]) < (data['High'].iloc[i-1] - data['Low'].iloc[i-1]) * 0.1  # Bougie petite
    third_candle = data['Close'].iloc[i] > data['Open'].iloc[i]  # Troisième bougie haussière
    return first_candle and second_candle and third_candle

# Fonction pour identifier l'étoile du soir
def is_evening_star(data, i):
    if i < 2:
        return False
    # Conditions pour l'étoile du soir
    first_candle = data['Close'].iloc[i-2] > data['Open'].iloc[i-2]  # Première bougie haussière
    second_candle = abs(data['Close'].iloc[i-1] - data['Open'].iloc[i-1]) < (data['High'].iloc[i-1] - data['Low'].iloc[i-1]) * 0.1  # Bougie petite
    third_candle = data['Close'].iloc[i] < data['Open'].iloc[i]  # Troisième bougie baissière
    return first_candle and second_candle and third_candle

# Détection des motifs dans les données
morning_stars = []
evening_stars = []

for i in range(2, len(data)):
    if is_morning_star(data, i):
        morning_stars.append(i)
    if is_evening_star(data, i):
        evening_stars.append(i)

# Préparer les données à afficher pour les motifs
highlight_morning_dates = data.index[morning_stars]
highlight_morning_values = data['Low'].iloc[morning_stars]

highlight_evening_dates = data.index[evening_stars]
highlight_evening_values = data['High'].iloc[evening_stars]

# Assurez-vous que les valeurs et dates sont alignées pour les motifs
highlight_morning = mpf.make_addplot(highlight_morning_values, type='scatter', markersize=100, marker='^', color='g')
highlight_evening = mpf.make_addplot(highlight_evening_values, type='scatter', markersize=100, marker='v', color='r')

# Tracer les chandelles avec les motifs identifiés
mpf.plot(data, type='candle', style='charles', title="Chandeliers Japonais avec Patterns",
         ylabel='Prix', volume=True, addplot=[highlight_morning, highlight_evening])

# Afficher les indices des motifs détectés
print("Indices des étoiles du matin détectées : ", morning_stars)
print("Indices des étoiles du soir détectées : ", evening_stars)
