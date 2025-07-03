import plotly.graph_objs as go
import plotly.io as pio

def plot_price_and_sma(df):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"],y=df["Close"],mode="lines",name="Close"))
    if "SMA20" in df.columns:
        fig.add_trace(go.Scatter(x=df["Date"],y=df["SMA20"],mode="lines",name="SMA 20"))
    fig.update_layout(title="Stock Price with SMA",xaxis_title="Date",yaxis_title="Price")
    return pio.to_html(fig,full_html=False)

def plot_rsi(df):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"],y=df["RSI14"],mode="lines",name="RSI"))
    fig.update_layout(title="RSI (Relative Strength Index)",xaxis_title="Date",yaxis_title="RSI",yaxis_range=[0,100])
    return pio.to_html(fig,full_html=False)

def plot_macd(df):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"],y=df["MACD"],mode="lines",name="MACD Line"))
    fig.add_trace(go.Scatter(x=df["Date"],y=df["Signal"],mode="lines",name="Signal Line"))
    fig.update_layout(title="MACD",xaxis_title="Date",yaxis_title="Value")
    return pio.to_html(fig,full_html=False)
