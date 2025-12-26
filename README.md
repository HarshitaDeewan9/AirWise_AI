# 🌍 AIRWISE — Smart Air Quality Intelligence Platform

AIRWISE is an AI-powered air quality monitoring, forecasting, and health-awareness platform that combines real-time pollution data, machine learning, and generative AI to deliver actionable insights for citizens, researchers, and policymakers.

---

## 🚀 Key Features

### 📈 AQI Forecasting
- Uses OpenWeather Air Pollution API
- Machine learning–based AQI prediction
- Trained on historical AQI and weather data
- City-level forecasting

### 🤖 AI Assistant (Gemini 2.5 Flash)
- Explains current and predicted AQI
- Identifies dominant pollutants
- Provides health and safety guidance
- Clearly distinguishes live vs simulated data

### ❤️ Personalized Health Risk Analysis
- Factors in AQI, age, and respiratory conditions
- ML-based risk scoring trained on synthetic data
- Awareness-focused (not medical diagnosis)

### 🕵️ Pollution Source Attribution
- Estimates contribution from:
  - Traffic
  - Industry
  - Biomass burning
  - Dust and natural sources
- Based on pollutant composition patterns

### 🎨 Modern UI
- Dark blue gradient theme
- Card-based layout
- Responsive Streamlit interface

---

## 🧠 Technology Stack

- Frontend: Streamlit
- Backend: Python
- API: OpenWeather (Air Pollution & Weather)
- Machine Learning: Scikit-learn, XGBoost
- Data Processing: Pandas, NumPy
- Generative AI: Google Gemini 2.5 Flash
- Deployment: Streamlit Community Cloud

---

## 🔑 API Keys Required

### OpenWeather API
Used for air pollution and weather data  
https://openweathermap.org/api

### Google Gemini API
Used for AI explanations  
https://ai.google.dev/

---

## 🔐 Secrets Configuration

### `.streamlit/secrets.toml`
```toml
OPENWEATHER_API_KEY = "your_openweather_api_key"
GEMINI_API_KEY = "your_gemini_api_key"
```

🛠️ Local Setup

1. cd AirWise_AI
2. pip install -r requirements.txt
3. streamlit run Home.py

## 📊 AQI Scale
OpenWeather AQI:

Value -> Meaning
- 1	-> Good
- 2	-> Fair
- 3	-> Moderate
- 4	-> Poor
- 5	-> Very Poor

Internally scaled to a 0–300 range for modeling and health analysis.

⚠️ Data Reliability Policy
- Live data is clearly marked as LIVE
- API failures fall back to simulated data
- Simulated data is always labeled
- AIRWISE never silently substitutes data.

⚠️ Disclaimer
AIRWISE provides informational insights only.
It is not a medical diagnostic or advisory tool.

🌱 Future Roadmap
- Satellite pollution data
- Improved source attribution models
- City-level alerts
- Mobile-friendly UI

AIRWISE © 2025 — Built for clean air awareness and AI-driven public health insights
