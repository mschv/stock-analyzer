import yfinance as yf
import pandas as pd

def get_stock_data(ticker:str,period:str="6mo",interval:str="1d")->pd.DataFrame:
    """
    Fetch historical stock data using yfinance.

    Args:
        ticker (str): Stock symbol (e.g., 'AAPL').
        period (str): Period to retrieve (e.g., '1mo', '6mo', '1y', 'max').
        interval (str): Data interval (e.g., '1d', '1wk', '1mo').

    Returns:
        pd.DataFrame: Historical stock price data.
    """
    try:
        stock=yf.Ticker(ticker)
        df=stock.history(period=period,interval=interval)
        if df.empty:
            raise ValueError("No data found for ticker.")
        df.reset_index(inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for {ticker}:{e}")
        return pd.DataFrame()