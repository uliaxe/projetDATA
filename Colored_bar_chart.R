
categories <- c("A", "B", "C", "D")
values <- c(3, 7, -5, 2)  # Données avec variations positives et négatives
colors <- ifelse(values > 0, "green", "red")  # Couleurs selon la valeur

barplot(values, names.arg = categories, col = colors, main = "Diagramme en Barres Colorées",
        xlab = "Catégories", ylab = "Valeurs")
