import streamlit as st
from services.data_loader import fetch_openweather_aqi
from models.health_risk import health_risk_score
from services.aqi_utils import openweather_to_us_aqi

# ----------------------------------
# UI
# ----------------------------------
st.set_page_config(page_title="Health Risk", page_icon="❤️")
st.title("❤️ Personal Health Risk")

city = st.text_input("City", "Delhi")
age = st.slider("Age", 1, 100, 30)
condition = st.checkbox("Respiratory Condition")

# ----------------------------------
# City → Coordinates (SAFE MAP)
# ----------------------------------
CITY_COORDS = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
}

lat, lon = CITY_COORDS.get(city, CITY_COORDS["Delhi"])

# ----------------------------------
# Fetch live AQI (OpenWeather)
# ----------------------------------
try:
    df = fetch_openweather_aqi(lat, lon, hours=24)
    raw_aqi = int(df["aqi"].iloc[-1])
    current_aqi=openweather_to_us_aqi(raw_aqi)
    st.success("✅ Using live OpenWeather AQI data")
except Exception:
    current_aqi = 180
    st.warning("⚠️ Using fallback AQI data")

# ----------------------------------
# ML-based Health Risk
# ----------------------------------
risk = health_risk_score(
    aqi=current_aqi,
    age=age,
    condition=condition
)

# ----------------------------------
# Output
# ----------------------------------
st.metric("Current AQI", current_aqi)
st.metric("Health Risk Score", f"{risk}/100")