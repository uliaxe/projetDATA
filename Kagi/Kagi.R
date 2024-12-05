library(quantmod)

# Exemple fictif de données de prix (OHLC)
data <- data.frame(
  Open = c(100, 102, 104, 103, 105, 102, 98, 101),
  High = c(102, 104, 106, 105, 108, 103, 99, 102),
  Low = c(99, 101, 103, 102, 104, 100, 96, 98),
  Close = c(101, 103, 105, 104, 102, 99, 97, 100)
)
xts_data <- xts(data, order.by = as.Date("2023-01-01") + 0:7)

# Fonction manuelle pour tracer un graphique Kagi (simplifié)
kagiChart <- function(data, reversal = 2) {
  plot(data$Close, type = "l", col = "blue", main = "Graphique Kagi (simplifié)",
       xlab = "Temps", ylab = "Prix")
  abline(h = seq(min(data$Close), max(data$Close), by = reversal), col = "gray", lty = 2)
}

# Affichage
kagiChart(xts_data)
