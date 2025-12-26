import requests
import pandas as pd
from datetime import datetime
import streamlit as st

OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]

def geocode_city(city: str):
    """
    Convert city name to latitude & longitude using OpenWeather
    """
    url = "http://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": city,
        "limit": 1,
        "appid": OPENWEATHER_API_KEY
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    if not data:
        raise ValueError("City not found")

    return data[0]["lat"], data[0]["lon"]

# -------------------------------------------------
# Load API key safely
# -------------------------------------------------
OPENWEATHER_API_KEY = st.secrets.get("OPENWEATHER_API_KEY")

if not OPENWEATHER_API_KEY:
    raise RuntimeError("❌ OPENWEATHER_API_KEY not found in Streamlit secrets")

# -------------------------------------------------
# Fetch historical AQI (hourly)
# -------------------------------------------------
def fetch_openweather_aqi(lat: float, lon: float, hours: int = 72) -> pd.DataFrame:
    """
    Fetch historical AQI data from OpenWeather (hourly)
    """

    url = "https://api.openweathermap.org/data/2.5/air_pollution/history"

    end_ts = int(pd.Timestamp.utcnow().timestamp())
    start_ts = end_ts - hours * 3600

    params = {
        "lat": lat,
        "lon": lon,
        "start": start_ts,
        "end": end_ts,
        "appid": OPENWEATHER_API_KEY,
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()

    payload = r.json()
    data = payload.get("list", [])

    if not data:
        raise ValueError("No AQI history returned from OpenWeather")

    rows = []
    for item in data:
        rows.append({
            "datetime": datetime.utcfromtimestamp(item["dt"]),
            "aqi": item["main"]["aqi"],          # AQI scale 1–5
            "co": item["components"].get("co"),
            "no2": item["components"].get("no2"),
            "pm2_5": item["components"].get("pm2_5"),
            "pm10": item["components"].get("pm10"),
            "so2": item["components"].get("so2"),
        })

    df = pd.DataFrame(rows).set_index("datetime").sort_index()
    return df


# -------------------------------------------------
# Fetch current weather
# -------------------------------------------------
def fetch_weather(lat: float, lon: float) -> dict:
    """
    Fetch current weather from OpenWeather
    """

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()

    data = r.json()

    return {
        "wind": data["wind"]["speed"],
        "humidity": data["main"]["humidity"],
        "temp": data["main"]["temp"]
    }

import requests
import streamlit as st

OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]

def fetch_openweather_pollution(city: str) -> dict:
    """
    Fetch current air pollution data from OpenWeather
    Returns structured pollutant dictionary + AQI
    """

    # 1️⃣ Geocoding (city → lat/lon)
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    geo_params = {
        "q": city,
        "limit": 1,
        "appid": OPENWEATHER_API_KEY
    }

    geo_resp = requests.get(geo_url, params=geo_params, timeout=10)
    geo_resp.raise_for_status()
    geo_data = geo_resp.json()

    if not geo_data:
        raise ValueError("City not found")

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # 2️⃣ Air pollution data
    air_url = "http://api.openweathermap.org/data/2.5/air_pollution"
    air_params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY
    }

    air_resp = requests.get(air_url, params=air_params, timeout=10)
    air_resp.raise_for_status()
    air_data = air_resp.json()["list"][0]

    components = air_data["components"]

    pollutants = {
        "co":   {"value": components.get("co"),   "unit": "µg/m³"},
        "no2":  {"value": components.get("no2"),  "unit": "µg/m³"},
        "pm25": {"value": components.get("pm2_5"),"unit": "µg/m³"},
        "pm10": {"value": components.get("pm10"), "unit": "µg/m³"},
        "so2":  {"value": components.get("so2"),  "unit": "µg/m³"},
        "o3":   {"value": components.get("o3"),   "unit": "µg/m³"},
    }

    return {
        "source": "LIVE",
        "lat": lat,
        "lon": lon,
        "aqi": air_data["main"]["aqi"],  # OpenWeather AQI (1–5)
        "pollutants": pollutants
    }