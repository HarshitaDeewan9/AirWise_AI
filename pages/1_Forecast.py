import streamlit as st
import pandas as pd

from services.data_loader import fetch_openweather_aqi, fetch_weather
from services.feature_engineering import build_features
from services.aqi_utils import openweather_to_us_aqi
from models.aqi_forecast import train_model
from services.gemini_service import explain_aqi
from services.data_loader import geocode_city

# -------------------------------------------------
# UI
# -------------------------------------------------
st.set_page_config(page_title="AQI Forecast", page_icon="📈")
st.title("📈 AQI Forecast")

city = st.text_input("City", "Delhi")

try:
    LAT, LON = geocode_city(city)
    location_source = "LIVE"
except Exception:
    LAT, LON = 28.61, 77.20
    location_source = "FALLBACK"


# -------------------------------------------------
# FETCH AQI HISTORY
# -------------------------------------------------
try:
    raw_df = fetch_openweather_aqi(LAT, LON, hours=96)
    source = "LIVE"
except Exception:
    st.warning("Using fallback AQI data")
    source = "DUMMY"

    dates = pd.date_range(end=pd.Timestamp.utcnow(), periods=96, freq="H")
    raw_df = pd.DataFrame(
        {"aqi": [3] * 96},
        index=dates
    )

# -------------------------------------------------
# WEATHER
# -------------------------------------------------
try:
    weather = fetch_weather(LAT, LON)
except Exception:
    weather = {"wind": 2.5, "humidity": 60}

# -------------------------------------------------
# FEATURE ENGINEERING (🔥 FIX)
# -------------------------------------------------
df = build_features(raw_df, weather)

# -------------------------------------------------
# TRAIN MODEL
# -------------------------------------------------
model = train_model(df)

FEATURES = [
    "aqi_lag_1", "aqi_lag_3", "aqi_lag_6",
    "aqi_roll_3", "aqi_roll_6",
    "hour", "dayofweek", "wind", "humidity"
]

prediction_ow = int(
    model.predict(df[FEATURES].iloc[-1:].values)[0]
)

current_ow = int(raw_df["aqi"].iloc[-1])

# -------------------------------------------------
# CONVERT TO HUMAN AQI
# -------------------------------------------------
prediction_us = openweather_to_us_aqi(prediction_ow)
current_us = openweather_to_us_aqi(current_ow)

# -------------------------------------------------
# UI OUTPUT
# -------------------------------------------------
st.success(f"Data source: {source} | Location: {location_source}")

st.metric("Current AQI", current_us)
st.metric("Predicted AQI (Next Hour)", prediction_us)

st.info(
    explain_aqi(
        prediction=prediction_us,
        weather=weather,
        city=city
    )
)
