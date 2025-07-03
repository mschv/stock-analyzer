import pandas as pd

def calculate_sma(df: pd.DataFrame, window: int=20)->pd.Series:
    return df['Close'].rolling(window=window).mean()

def calculate_ema(df:pd.DataFrame,span: int=20)->pd.Series:
    return df['Close'].ewm(span=span,adjust=False).mean()

def calculate_rsi(df:pd.DataFrame,window:int=14)->pd.Series:
    delta=df['Close'].diff()
    gain=delta.clip(lower=0)
    loss=-delta.clip(upper=0)
    avg_gain=gain.rolling(window=window).mean()
    avg_loss=loss.rolling(window=window).mean()
    rs=avg_gain/(avg_loss+1e-10) #avoid division by zero
    return 100-(100/(1+rs))

def calculate_macd(df:pd.DataFrame,span_short=12,span_long=26,signal_span=9):
    ema_short=df['Close'].ewm(span=span_short,adjust=False).mean()
    ema_long=df['Close'].ewm(span=span_long,adjust=False).mean()
    macd_line=ema_short-ema_long
    signal_line=macd_line.ewm(span=signal_span,adjust=False).mean()
    return macd_line,signal_line