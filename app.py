from flask import Flask, render_template, request
from utils.fetch_data import get_stock_data
from analysis.indicators import calculate_sma, calculate_rsi, calculate_macd
from analysis.plot_stock import plot_price_and_sma, plot_rsi, plot_macd
from analysis.portfolio import (
    calculate_daily_returns,
    calculate_cumulative_return,
    calculate_volatility,
    calculate_sharpe_ratio,
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    charts = {}
    symbol = None
    cumulative = volatility = sharpe = None

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        df = get_stock_data(symbol)

        if not df.empty:
            df["SMA20"] = calculate_sma(df, 20)
            df["RSI14"] = calculate_rsi(df, 14)
            df["MACD"], df["Signal"] = calculate_macd(df)

            charts["price"] = plot_price_and_sma(df)
            charts["rsi"] = plot_rsi(df)
            charts["macd"] = plot_macd(df)

            returns = calculate_daily_returns(df)
            cumulative = round(calculate_cumulative_return(df) * 100, 2)
            volatility = round(calculate_volatility(returns) * 100, 2)
            sharpe = round(calculate_sharpe_ratio(returns), 2)

    return render_template("index.html", symbol=symbol, charts=charts,
                           cumulative=cumulative, volatility=volatility, sharpe=sharpe)

if __name__ == "__main__":
    app.run(debug=True)
