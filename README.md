# 📈 Sensex Stock Fetcher

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A real-time financial data visualization application that fetches and displays live stock market data for all 30 Sensex companies. Built with Python, Streamlit, and Yahoo Finance API, this application provides an intuitive dashboard for monitoring Indian stock market performance.

## 🚀 Features

- **Real-time Data Fetching**: Live stock data from Yahoo Finance API
- **Interactive Dashboard**: Clean, responsive web interface built with Streamlit
- **Comprehensive Coverage**: All 30 Sensex companies included
- **Visual Analytics**: Color-coded performance indicators and summary statistics
- **Top Performers Tracking**: Automatic identification of top gainers and losers
- **Responsive Design**: Optimized for various screen sizes
- **Auto-refresh Capability**: Manual refresh button for latest data

## 🏗️ Architecture

### System Design
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend        │    │   Data Source   │
│   (Streamlit)   │◄──►│   (Python)       │◄──►│   (Yahoo Finance)│
│                 │    │                  │    │                 │
│ • Dashboard UI  │    │ • Data Processing│    │ • Real-time API │
│ • Visualization │    │ • Error Handling │    │ • Historical Data│
│ • User Controls │    │ • Data Validation│    │ • Market Data   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Key Components

1. **Data Layer** (`Sensex_yfinance.py`)
   - Handles raw data fetching from Yahoo Finance
   - Implements error handling for API failures
   - Manages data validation and preprocessing

2. **Application Layer** (`app.py`)
   - Streamlit web application framework
   - Real-time data visualization
   - User interface and interaction handling

3. **Presentation Layer**
   - Interactive tables with conditional formatting
   - Summary statistics and metrics
   - Responsive design with custom CSS styling

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework for rapid prototyping
- **yfinance**: Yahoo Finance API wrapper for financial data
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualization (imported for future enhancements)
- **NumPy**: Numerical computing support

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection for API access

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sensex-fetcher.git
   cd sensex-fetcher
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`
   - The application will automatically fetch the latest stock data

3. **Features to explore**
   - View real-time stock prices for all 30 Sensex companies
   - Check percentage changes with color-coded indicators
   - Monitor top gainers and losers
   - Use the refresh button to get the latest data

## 📊 Data Structure

The application processes the following data points for each stock:
- **Symbol**: Company ticker symbol (e.g., RELIANCE.NS)
- **Starting Price**: Opening price for the day
- **Closing Price**: Current/latest price
- **Change %**: Percentage change from opening to current price

## 🎯 Key Skills Demonstrated

### Backend Development
- **API Integration**: Seamless integration with Yahoo Finance API
- **Data Processing**: Efficient handling of financial data using Pandas
- **Error Handling**: Robust error handling for API failures and data validation
- **Performance Optimization**: Efficient data fetching and processing

### Frontend Development
- **Web Application Development**: Modern web interface using Streamlit
- **User Experience Design**: Intuitive dashboard with responsive design
- **Data Visualization**: Interactive tables with conditional formatting
- **CSS Styling**: Custom styling for enhanced user experience

### Software Architecture
- **Modular Design**: Separation of concerns between data fetching and presentation
- **Scalable Structure**: Easy to extend with additional features
- **Clean Code**: Well-organized, readable, and maintainable codebase
- **Dependency Management**: Proper requirements management

### Financial Domain Knowledge
- **Market Understanding**: Comprehensive coverage of Sensex constituents
- **Data Analysis**: Real-time performance tracking and analytics
- **Financial Metrics**: Proper calculation of percentage changes and statistics

## 🔧 Configuration

The application can be easily configured by modifying the following:

- **Stock List**: Update `sensex_tickers` list in both files to include/exclude companies
- **Data Period**: Modify the `period` parameter in `stock.history()` for different timeframes
- **Styling**: Customize the CSS in the Streamlit app for different themes

## 🚀 Future Enhancements

- [ ] Historical data visualization with interactive charts
- [ ] Portfolio tracking and management features
- [ ] Real-time notifications for significant price movements
- [ ] Export functionality for data analysis
- [ ] Mobile-responsive design improvements
- [ ] Caching mechanism for improved performance
- [ ] User authentication and personalized dashboards

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) for providing the financial data API
- [Streamlit](https://streamlit.io/) for the excellent web application framework
- [yfinance](https://github.com/ranaroussi/yfinance) for the Python wrapper
- The open-source community for the amazing tools and libraries



⭐ **Star this repository if you found it helpful!**
