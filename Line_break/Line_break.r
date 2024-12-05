# Exemple fictif de données de prix de clôture
close_prices <- c(100, 102, 104, 103, 105, 102, 98, 101)

# Fonction pour calculer les blocs Line Break
line_break_chart <- function(prices, n = 3) {
  blocks <- numeric()
  for (i in 2:length(prices)) {
    if (length(blocks) < n || prices[i] > max(tail(blocks, n))) {
      blocks <- c(blocks, prices[i])  # Ajout d'un bloc haussier
    } else if (prices[i] < min(tail(blocks, n))) {
      blocks <- c(blocks, prices[i])  # Ajout d'un bloc baissier
    }
  }
  blocks
}

# Calcul des blocs et affichage
blocks <- line_break_chart(close_prices)
plot(blocks, type = "b", col = "blue", pch = 19, lwd = 2, main = "Graphique Line Break",
     xlab = "Mouvement", ylab = "Prix")
grid()
