import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, -5, 2]  # Données avec des variations positives et négatives
colors = ['green' if v > 0 else 'red' for v in values]  # Attribuer une couleur selon la valeur

plt.bar(categories, values, color=colors)  # Création du diagramme
plt.title("Diagramme en Barres Colorées")
plt.xlabel("Catégories")
plt.ylabel("Valeurs")
plt.show()
