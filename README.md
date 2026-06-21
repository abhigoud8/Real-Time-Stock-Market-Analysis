# Real-Time Stock Market Analysis

![Python](https://img.shields.io/badge/Python-3.9-blue) ![Plotly](https://img.shields.io/badge/Plotly-5.17-purple) ![yfinance](https://img.shields.io/badge/yfinance-0.2-green)

## Overview
A comprehensive stock market analysis tool that fetches real-time and historical data, performs technical analysis, and generates interactive visualizations to assist with investment decisions.

## Features
- Real-time stock data fetching using yfinance
- Moving averages: SMA, EMA (20, 50, 200 day)
- RSI, MACD, Bollinger Bands indicators
- Portfolio performance tracking
- Interactive Plotly candlestick charts
- Correlation heatmap between multiple stocks

## Tech Stack
- **Python** — pandas, numpy, yfinance
- **Visualization** — Plotly, matplotlib
- **Dashboard** — Streamlit

## Project Structure
```
Real-Time-Stock-Market-Analysis/
├── src/
│   ├── fetch_data.py      # Data fetching from yfinance
│   ├── indicators.py      # Technical indicators
│   └── dashboard.py       # Streamlit dashboard
├── notebooks/             # Analysis notebooks
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
```

## Sample Output
Candlestick charts with SMA/EMA overlays, volume bars, and RSI/MACD subplots for stocks like AAPL, TSLA, MSFT, AMZN.