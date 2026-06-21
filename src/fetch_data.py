import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def fetch_stock(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.index = pd.to_datetime(df.index)
    return df

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["EMA_20"] = df["Close"].ewm(span=20, adjust=False).mean()
    # RSI
    delta = df["Close"].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    df["RSI"] = 100 - (100 / (1 + gain / loss))
    # MACD
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema12 - ema26
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
    return df

def plot_stock(ticker: str):
    df = add_indicators(fetch_stock(ticker))
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        row_heights=[0.6, 0.2, 0.2],
                        subplot_titles=[f"{ticker} Price", "RSI", "MACD"])
    fig.add_trace(go.Candlestick(x=df.index, open=df["Open"], high=df["High"],
                                  low=df["Low"], close=df["Close"], name="Price"), row=1, col=1)
    for ma in ["SMA_20", "SMA_50", "EMA_20"]:
        fig.add_trace(go.Scatter(x=df.index, y=df[ma], name=ma), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df["RSI"], name="RSI", line=dict(color="orange")), row=2, col=1)
    fig.add_trace(go.Bar(x=df.index, y=df["MACD"] - df["Signal"], name="MACD Hist"), row=3, col=1)
    fig.update_layout(title=f"{ticker} Technical Analysis", height=800, xaxis_rangeslider_visible=False)
    fig.show()

if __name__ == "__main__":
    for ticker in ["AAPL", "TSLA", "MSFT"]:
        plot_stock(ticker)