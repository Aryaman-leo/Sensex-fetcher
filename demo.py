#!/usr/bin/env python3
"""
Demo script for Sensex Stock Fetcher
This script demonstrates the core functionality without the Streamlit UI
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
import time

def demo_sensex_fetcher():
    """
    Demonstrate the core functionality of the Sensex Stock Fetcher
    """
    print("📈 Sensex Stock Fetcher - Demo Mode")
    print("=" * 50)
    
    # List of Sensex company ticker symbols
    sensex_tickers = [
        "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "HINDUNILVR.NS", "INFY.NS", 
        "ICICIBANK.NS", "HDFC.NS", "BAJFINANCE.NS", "KOTAKBANK.NS", "SBIN.NS",
        "LT.NS", "AXISBANK.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "ITC.NS",
        "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "MARUTI.NS", "NESTLEIND.NS",
        "TITAN.NS", "INDUSINDBK.NS", "POWERGRID.NS", "BAJAJFINSV.NS", "NTPC.NS",
        "TECHM.NS", "M&M.NS", "TATASTEEL.NS", "ONGC.NS", "HEROMOTOCO.NS"
    ]
    
    print(f"Fetching data for {len(sensex_tickers)} Sensex companies...")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Fetch data for each ticker
    data = []
    successful_fetches = 0
    
    for i, ticker in enumerate(sensex_tickers, 1):
        try:
            print(f"[{i:2d}/{len(sensex_tickers)}] Fetching {ticker}...", end=" ")
            
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            
            if not hist.empty:
                start_price = hist['Open'][0]
                close_price = hist['Close'][0]
                change = ((close_price - start_price) / start_price) * 100
                data.append([ticker, start_price, close_price, change])
                successful_fetches += 1
                print(f"✓ (₹{close_price:.2f}, {change:+.2f}%)")
            else:
                print("✗ (No data)")
                
        except Exception as e:
            print(f"✗ (Error: {str(e)[:30]}...)")
        
        # Small delay to avoid rate limiting
        time.sleep(0.1)
    
    print("-" * 50)
    print(f"Successfully fetched data for {successful_fetches}/{len(sensex_tickers)} companies")
    
    if data:
        # Create DataFrame
        df = pd.DataFrame(data, columns=['Symbol', 'Starting Price', 'Closing Price', 'Change %'])
        
        # Display summary
        print("\n📊 Summary Statistics:")
        print(f"Average Change: {df['Change %'].mean():.2f}%")
        print(f"Best Performer: {df.loc[df['Change %'].idxmax(), 'Symbol']} ({df['Change %'].max():.2f}%)")
        print(f"Worst Performer: {df.loc[df['Change %'].idxmin(), 'Symbol']} ({df['Change %'].min():.2f}%)")
        
        # Display top 5 gainers
        print("\n🚀 Top 5 Gainers:")
        top_gainers = df.nlargest(5, 'Change %')
        for _, row in top_gainers.iterrows():
            print(f"  {row['Symbol']:15} ₹{row['Closing Price']:8.2f} ({row['Change %']:+6.2f}%)")
        
        # Display top 5 losers
        print("\n📉 Top 5 Losers:")
        top_losers = df.nsmallest(5, 'Change %')
        for _, row in top_losers.iterrows():
            print(f"  {row['Symbol']:15} ₹{row['Closing Price']:8.2f} ({row['Change %']:+6.2f}%)")
        
        print("\n" + "=" * 50)
        print("Demo completed successfully! 🎉")
        print("Run 'streamlit run app.py' to see the full interactive dashboard.")
        
    else:
        print("❌ No data could be fetched. Please check your internet connection.")

if __name__ == "__main__":
    try:
        demo_sensex_fetcher()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        print("Please ensure all dependencies are installed: pip install -r requirements.txt")
