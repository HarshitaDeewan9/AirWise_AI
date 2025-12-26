import streamlit as st

from services.data_loader import fetch_openweather_aqi, fetch_weather
from services.gemini_service import ask_gemini
from services.aqi_utils import openweather_to_us_aqi

# -------------------------------------------------
# PAGE SETUP
# -------------------------------------------------
st.set_page_config(page_title="AIRWISE AI", page_icon="💬")
st.title("💬 AIRWISE AI Assistant")

city = st.text_input("City", "Delhi")

LAT, LON = 28.61, 77.20

# -------------------------------------------------
# HARD DUMMY CONTEXT (SAFE)
# -------------------------------------------------
DUMMY_CONTEXT = {
    "city": city,
    "current_aqi": 150,
    "predicted_aqi": 180,
    "wind": 2.5,
    "humidity": 60,
    "source": "DUMMY"
}

# -------------------------------------------------
# CONTEXT FETCH
# -------------------------------------------------
@st.cache_data(ttl=1800)
def get_context():
    try:
        df = fetch_openweather_aqi(LAT, LON, hours=48)
        weather = fetch_weather(LAT, LON)

        current_ow = int(df["aqi"].iloc[-1])
        current_us = openweather_to_us_aqi(current_ow)

        # Simple persistence prediction (placeholder)
        predicted_us = openweather_to_us_aqi(current_ow)

        return {
            "city": city,
            "current_aqi": current_us,
            "predicted_aqi": predicted_us,
            "wind": weather["wind"],
            "humidity": weather["humidity"],
            "source": "LIVE"
        }

    except Exception:
        return DUMMY_CONTEXT


context = get_context()

# -------------------------------------------------
# SOURCE INDICATOR
# -------------------------------------------------
if context["source"] == "LIVE":
    st.success("✅ Using live OpenWeather data")
else:
    st.warning("⚠️ Using simulated data")

# -------------------------------------------------
# SYSTEM PROMPT
# -------------------------------------------------
def build_system_prompt(ctx):
    return f"""
You are AIRWISE AI, an air-quality expert.

DATA SOURCE: {ctx['source']}
CITY: {ctx['city']}

CURRENT AQI: {ctx['current_aqi']}
PREDICTED AQI (next period): {ctx['predicted_aqi']}

WEATHER:
Wind Speed: {ctx['wind']} m/s
Humidity: {ctx['humidity']} %

Rules:
- Use ONLY provided data
- Explain AQI clearly
- Identify trends (improving/worsening)
- Avoid medical diagnosis
- Give general safety advice
"""

# -------------------------------------------------
# CHAT MEMORY
# -------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("🗑️ Clear Conversation"):
    st.session_state.chat_history = []
    st.rerun()

# -------------------------------------------------
# CHAT INPUT
# -------------------------------------------------
user_input = st.text_input("Ask about air quality, health, or precautions")

if user_input:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    prompt = build_system_prompt(context) + "\n\n"

    for msg in st.session_state.chat_history:
        prompt += f"{msg['role'].upper()}: {msg['content']}\n"

    prompt += "\nASSISTANT:"

    response = ask_gemini(prompt)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": response}
    )

# -------------------------------------------------
# DISPLAY CHAT
# -------------------------------------------------
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 AIRWISE:** {msg['content']}")
