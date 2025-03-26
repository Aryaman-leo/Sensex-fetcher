import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Sensex Stock Fetcher",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide the default Streamlit elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    header {visibility: hidden;}
    .stAppHeader {display: none;}
    .stToolbar {display: none;}
    .stAppToolbar {display: none;}
    .stToolbarActions {display: none;}
    .stAppDeployButton {display: none;}
    .stMainMenu {display: none;}
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("📈 Sensex Stock Fetcher")
st.markdown("Real-time data for Sensex companies")

# List of Sensex company ticker symbols
sensex_tickers = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "HINDUNILVR.NS", "INFY.NS", 
    "ICICIBANK.NS", "HDFC.NS", "BAJFINANCE.NS", "KOTAKBANK.NS", "SBIN.NS",
    "LT.NS", "AXISBANK.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "ITC.NS",
    "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "MARUTI.NS", "NESTLEIND.NS",
    "TITAN.NS", "INDUSINDBK.NS", "POWERGRID.NS", "BAJAJFINSV.NS", "NTPC.NS",
    "TECHM.NS", "M&M.NS", "TATASTEEL.NS", "ONGC.NS", "HEROMOTOCO.NS"
]

def fetch_stock_data():
    with st.spinner('Fetching latest stock data...'):
        data = []
        for ticker in sensex_tickers:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            if not hist.empty:
                start_price = hist['Open'][0]
                close_price = hist['Close'][0]
                change = ((close_price - start_price) / start_price) * 100
                data.append([ticker, start_price, close_price, change])
        
        df = pd.DataFrame(data, columns=['Symbol', 'Starting Price', 'Closing Price', 'Change %'])
        return df

# Add refresh button
if st.button("🔄 Refresh Data"):
    st.rerun()

# Fetch and display data
df = fetch_stock_data()

# Display current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"Last updated: {current_time}")

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    # Display the main table with styling
    st.markdown("### Stock Data")
    styled_df = df.style.format({
        'Starting Price': '₹{:.2f}',
        'Closing Price': '₹{:.2f}',
        'Change %': '{:.2f}%'
    }).background_gradient(subset=['Change %'], cmap='RdYlGn')
    st.dataframe(styled_df, use_container_width=True)

with col2:
    # Display summary statistics
    st.markdown("### Summary Statistics")
    
    # Display metrics that can be shown directly
    st.metric("Total Companies", len(df))
    st.metric("Average Change", f"{df['Change %'].mean():.2f}%")
    
    # Display top gainers and losers in a more appropriate format
    st.markdown("#### Top Gainers")
    top_gainers = df.nlargest(3, 'Change %')[['Symbol', 'Change %']]
    top_gainers['Change %'] = top_gainers['Change %'].apply(lambda x: f"{x:.2f}%")
    st.dataframe(top_gainers, hide_index=True)
    
    st.markdown("#### Top Losers")
    top_losers = df.nsmallest(3, 'Change %')[['Symbol', 'Change %']]
    top_losers['Change %'] = top_losers['Change %'].apply(lambda x: f"{x:.2f}%")
    st.dataframe(top_losers, hide_index=True)

# Footer
st.markdown("---")
st.markdown("Data source: Yahoo Finance") 