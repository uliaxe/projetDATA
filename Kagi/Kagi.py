import mplfinance as mpf
import pandas as pd

# Exemple fictif de données de prix (OHLC)
data = pd.DataFrame({
    'Open': [100, 102, 104, 103, 105, 102, 98, 101],
    'High': [102, 104, 106, 105, 108, 103, 99, 102],
    'Low': [99, 101, 103, 102, 104, 100, 96, 98],
    'Close': [101, 103, 105, 104, 102, 99, 97, 100],
}, index=pd.date_range("2023-01-01", periods=8))

# Graphique Kagi
mpf.plot(data, type='kagi', title="Graphique Kagi")
