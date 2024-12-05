library(quantmod)

# Fonction pour calculer les valeurs Heikin Ashi
heikin_ashi <- function(data) {
  ha_open <- c((data$Open[1] + data$Close[1]) / 2)  # Initialisation
  ha_data <- data.frame(
    Open = numeric(),
    High = numeric(),
    Low = numeric(),
    Close = numeric()
  )
  
  for (i in 1:nrow(data)) {
    ha_close <- (data$Open[i] + data$High[i] + data$Low[i] + data$Close[i]) / 4
    ha_open <- c(ha_open, (ha_open[length(ha_open)] + ha_close) / 2)
    ha_high <- max(data$High[i], ha_open[length(ha_open)], ha_close)
    ha_low <- min(data$Low[i], ha_open[length(ha_open)], ha_close)
    ha_data <- rbind(ha_data, c(Open = ha_open[length(ha_open)], High = ha_high, Low = ha_low, Close = ha_close))
  }
  
  xts(ha_data, order.by = index(data))
}

# Exemple fictif de données OHLC
data <- data.frame(
  Open = c(100, 102, 105, 103),
  High = c(105, 107, 108, 106),
  Low = c(98, 101, 103, 102),
  Close = c(104, 106, 104, 105)
)
xts_data <- xts(data, order.by = as.Date("2023-01-01") + 0:3)

# Calcul Heikin Ashi
ha_data <- heikin_ashi(xts_data)

# Graphique Heikin Ashi
candleChart(ha_data, main = "Graphique Heikin Ashi")
