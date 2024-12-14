import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Génération de données factices de prix (vous pouvez les remplacer par des données réelles)
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100, freq='B')  # 100 jours ouvrés
initial_price = 100
returns = np.random.normal(loc=0, scale=0.01, size=100)  # Rendements journaliers normalement distribués

# Calcul des prix à partir des rendements
prices = initial_price * (1 + returns).cumprod()  # Simuler les prix avec les rendements cumulés

# Calcul des rendements (pour reconstruire la distribution de probabilité)
daily_returns = np.diff(prices) / prices[:-1]

# Estimation de la distribution de probabilité des rendements
plt.figure(figsize=(10, 6))
plt.hist(daily_returns, bins=30, density=True, alpha=0.6, color='g')

# Tracer une courbe de distribution normale ajustée
from scipy.stats import norm

mu, std = norm.fit(daily_returns)  # Estimation des paramètres de la distribution normale
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Distribution de probabilité des rendements simulés (Marche aléatoire)')
plt.xlabel('Rendement')
plt.ylabel('Densité de probabilité')
plt.grid(True)
plt.show()

# Affichage de la moyenne et de l'écart-type
print(f"Moyenne des rendements : {mu:.4f}")
print(f"Écart-type des rendements : {std:.4f}")


