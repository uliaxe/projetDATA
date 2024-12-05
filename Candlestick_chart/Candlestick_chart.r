library(quantmod)

# Exemple fictif de données OHLC
data <- data.frame(
  Open = c(100, 102, 105, 103),
  High = c(105, 107, 108, 106),
  Low = c(98, 101, 103, 102),
  Close = c(104, 106, 104, 105)
)
xts_data <- xts(data, order.by = as.Date("2023-01-01") + 0:3)

# Graphique en bougies japonaises
candleChart(xts_data, type = "candles", main = "Graphique en Bougies Japonaises")
