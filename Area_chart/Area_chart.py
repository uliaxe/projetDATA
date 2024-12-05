import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)  # Points de 0 à 10
y = np.sin(x)  # Fonction sinusoïdale

plt.fill_between(x, y, color="skyblue", alpha=0.4)  # Remplir l'aire
plt.plot(x, y, color="Slateblue", alpha=0.8)  # Courbe principale
plt.title("Graphique d'Aire")  # Titre
plt.xlabel("Temps")
plt.ylabel("Amplitude")
plt.show()
