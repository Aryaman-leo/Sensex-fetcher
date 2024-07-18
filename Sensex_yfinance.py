import yfinance as yf
import pandas as pd

# List of Sensex company ticker symbols
sensex_tickers = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "HINDUNILVR.NS", "INFY.NS", 
    "ICICIBANK.NS", "HDFC.NS", "BAJFINANCE.NS", "KOTAKBANK.NS", "SBIN.NS",
    "LT.NS", "AXISBANK.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "ITC.NS",
    "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "MARUTI.NS", "NESTLEIND.NS",
    "TITAN.NS", "INDUSINDBK.NS", "POWERGRID.NS", "BAJAJFINSV.NS", "NTPC.NS",
    "TECHM.NS", "M&M.NS", "TATASTEEL.NS", "ONGC.NS", "HEROMOTOCO.NS"
]

# Initialize a list to store the data
data = []

# Fetch data for each ticker
for ticker in sensex_tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    if not hist.empty:
        start_price = hist['Open'][0]
        close_price = hist['Close'][0]
        data.append([ticker, start_price, close_price])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Symbol', 'Starting Price', 'Closing Price'])

# Print the DataFrame
print(df)
