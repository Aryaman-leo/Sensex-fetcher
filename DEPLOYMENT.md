# 🚀 Deployment Guide

This guide will help you deploy the Sensex Stock Fetcher application to various platforms.

## 📋 Prerequisites

- Python 3.8 or higher
- Git installed on your system
- Active internet connection

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit applications.

#### Steps:
1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and branch
   - Set the main file path to `app.py`
   - Click "Deploy!"

### 2. Heroku

#### Steps:
1. **Create a Procfile**
   ```bash
   echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile
   ```

2. **Create runtime.txt**
   ```bash
   echo "python-3.9.7" > runtime.txt
   ```

3. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### 3. Docker Deployment

#### Create Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

#### Build and run:
```bash
docker build -t sensex-fetcher .
docker run -p 8501:8501 sensex-fetcher
```

### 4. Local Development Server

#### Run locally:
```bash
streamlit run app.py
```

Access at: `http://localhost:8501`

## 🔧 Environment Variables

For production deployment, you might want to set these environment variables:

- `STREAMLIT_SERVER_PORT`: Port number (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: localhost)

## 📊 Performance Considerations

- **API Rate Limits**: Yahoo Finance has rate limits. Consider implementing caching for production use.
- **Memory Usage**: The application loads data for 30 companies simultaneously.
- **Update Frequency**: Consider implementing automatic refresh intervals.

## 🛡️ Security Notes

- The application only reads public financial data
- No sensitive information is stored or transmitted
- API calls are made directly from the client side

## 🔍 Monitoring

For production deployments, consider:
- Application performance monitoring
- Error logging and tracking
- Uptime monitoring
- API response time monitoring

## 📞 Support

If you encounter any deployment issues, please:
1. Check the application logs
2. Verify all dependencies are installed
3. Ensure internet connectivity for API access
4. Create an issue in the repository
