import streamlit as st
from services.data_loader import fetch_openweather_pollution
from models.source_attribution import estimate_sources

st.set_page_config(page_title="Source Analysis", page_icon="🕵️")
st.title("🕵️ Pollution Source Attribution")

city = st.text_input("City", "Delhi")

try:
    pollution = fetch_openweather_pollution(city)

    if pollution["source"] != "LIVE":
        raise ValueError("Fallback data")

    pollutants = pollution["pollutants"]
    source = "LIVE"

except Exception:
    pollutants = {
        "co": {"value": 800},
        "no2": {"value": 50},
        "pm25": {"value": 90},
        "pm10": {"value": 140},
        "so2": {"value": 20},
    }
    source = "DUMMY"

sources = estimate_sources(pollutants)

# ---------------- UI ----------------
if source == "LIVE":
    st.success("✅ Live source attribution based on pollutant composition")
else:
    st.warning("⚠️ Using simulated data")

st.bar_chart(sources)

st.caption(
    "Source contributions are inferred from pollutant composition, "
    "not directly measured. Values are indicative."
)