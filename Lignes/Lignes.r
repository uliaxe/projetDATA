# Données fictives
x <- c("Jan", "Feb", "Mar", "Apr", "May")
y <- c(100, 110, 105, 115, 120)

# Création du graphique en lignes
plot(y, type = "o", col = "blue", main = "Graphique en Lignes",
     xlab = "Mois", ylab = "Prix", xaxt = "n", lwd = 2)
axis(1, at = 1:5, labels = x)  # Ajouter les étiquettes pour l'axe des x
grid()
