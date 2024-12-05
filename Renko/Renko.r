# Données fictives de prix de clôture
close_prices <- c(100, 102, 104, 103, 105, 102, 98, 101)

# Fonction pour calculer les briques Renko
renko_chart <- function(prices, brick_size) {
  bricks <- c(prices[1])
  for (i in 2:length(prices)) {
    diff <- prices[i] - tail(bricks, 1)
    if (abs(diff) >= brick_size) {
      bricks <- c(bricks, tail(bricks, 1) + sign(diff) * brick_size)
    }
  }
  bricks
}

# Taille de la brique
brick_size <- 2

# Calcul des briques Renko
bricks <- renko_chart(close_prices, brick_size)

# Graphique Renko
plot(bricks, type = "s", col = "blue", lwd = 2, main = "Graphique Renko",
     xlab = "Mouvement", ylab = "Prix")
grid()
