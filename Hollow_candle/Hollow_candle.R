library(quantmod)

# Exemple fictif de données OHLC
data <- data.frame(
  Open = c(100, 102, 105, 103),
  High = c(105, 107, 108, 106),
  Low = c(98, 101, 103, 102),
  Close = c(104, 106, 104, 105)
)
xts_data <- xts(data, order.by = as.Date("2023-01-01") + 0:3)

# Fonction pour définir les couleurs et styles des bougies
addHollowCandle <- function(xts_data) {
  is_hollow <- xts_data$Close > xts_data$Open  # Détermine si la bougie est creuse
  candle_colors <- ifelse(is_hollow, "white", "red")  # Blanc pour creux, rouge pour rempli
  candleChart(xts_data, type = "candles", main = "Graphique Hollow Candle", up.col = "green", dn.col = "red", theme = "white")
}

# Affichage du graphique Hollow Candle
addHollowCandle(xts_data)
