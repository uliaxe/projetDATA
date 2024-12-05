import matplotlib.pyplot as plt

# Données fictives
x = ["Jan", "Feb", "Mar", "Apr", "May"]
y = [100, 110, 105, 115, 120]

# Création du graphique en lignes
plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Prix mensuel")
plt.title("Graphique en Lignes")
plt.xlabel("Mois")
plt.ylabel("Prix")
plt.legend()
plt.grid(alpha=0.5)
plt.show()
