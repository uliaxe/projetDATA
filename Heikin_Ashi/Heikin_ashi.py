import mplfinance as mpf
import pandas as pd

# Exemple fictif de données OHLC
data = pd.DataFrame({
    'Open': [100, 102, 105, 103],
    'High': [105, 107, 108, 106],
    'Low': [98, 101, 103, 102],
    'Close': [104, 106, 104, 105],
}, index=pd.date_range("2023-01-01", periods=4))

# Graphique en Heikin Ashi
mpf.plot(data, type='heikinashi', title="Graphique Heikin Ashi")
