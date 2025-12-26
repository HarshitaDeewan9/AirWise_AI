from google.genai import Client
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

client = Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-2.5-flash"


def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text.strip()


def explain_aqi(prediction: int, weather: dict, city: str) -> str:
    """
    Explains predicted AQI using Gemini
    Matches forecast page keyword arguments EXACTLY
    """

    wind = weather.get("wind", "unknown")
    humidity = weather.get("humidity", "unknown")

    prompt = f"""
You are an air quality expert.

City: {city}
Predicted AQI: {prediction}
Wind Speed: {wind} m/s
Humidity: {humidity} %

Explain:
1. What this AQI level means
2. Possible causes
3. Safety advice for the public

Keep it simple and practical.
"""

    return ask_gemini(prompt)
