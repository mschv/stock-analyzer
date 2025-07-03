from utils.fetch_data import get_stock_data
from analysis.indicators import calculate_sma, calculate_rsi, calculate_macd

df = get_stock_data("AAPL", period="3mo")

df["SMA20"] = calculate_sma(df, 20)
df["RSI14"] = calculate_rsi(df, 14)
df["MACD"], df["Signal"] = calculate_macd(df)

print(df[["Date", "Close", "SMA20", "RSI14", "MACD", "Signal"]].tail())

