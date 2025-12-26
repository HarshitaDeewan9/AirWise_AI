import streamlit as st

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="AIRWISE | Smart Air Quality Intelligence",
    page_icon="🌍",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS for dark blue gradient theme
# -------------------------------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Title text */
.main-title {
    font-size: 3.5rem;
    font-weight: 800;
    text-align: center;
    margin-top: 2rem;
    color: #e0f2ff;
}

/* Subtitle */
.subtitle {
    font-size: 1.3rem;
    text-align: center;
    margin-bottom: 3rem;
    color: #b6e0ff;
}

/* Card container */
.card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.8rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
    height: 100%;
}

/* Card title */
.card h3 {
    color: #d6f0ff;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 4rem;
    color: #aacbe1;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Hero Section
# -------------------------------------------------
st.markdown('<div class="main-title">🌍 AIRWISE</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Smart Air Quality Intelligence & Health-Aware AI Assistant</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# Description Section
# -------------------------------------------------
st.markdown("""
### 🔍 What is AIRWISE?

**AIRWISE** is an intelligent air-quality monitoring and forecasting platform that combines:

- 🌫️ **Air Quality Index (AQI) analytics**
- 📊 **Machine Learning–based forecasting**
- 🧠 **Generative AI (Gemini 2.5 Flash)**
- ❤️ **Health-aware recommendations**

It transforms complex pollution data into **actionable insights** for citizens, researchers, and policymakers.
""")

st.divider()

# -------------------------------------------------
# Feature Cards
# -------------------------------------------------
col1, col2 = st.columns(2)

st.markdown("<div style='height: 2rem'></div>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📈 AQI Forecasting</h3>
        <p>
        Predict future air quality trends using machine learning models trained
        on historical pollution and weather patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🤖 AI Assistant</h3>
        <p>
        Chat with an intelligent assistant grounded in real-time environmental
        data to understand health risks and safety measures.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>❤️ Health Risk Analysis</h3>
        <p>
        Get personalized health insights based on pollution exposure, age,
        and respiratory vulnerability.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>🕵️ Source Analysis</h3>
        <p>
        Identify likely pollution sources using pollutant composition
        and AI-driven heuristics.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# Tech Stack Section
# -------------------------------------------------
st.divider()

st.markdown("""
### 🛠️ Technology Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **API:** OpenWeather  
- **Generative AI:** Google Gemini 2.5 Flash

Designed with **scalability, reliability, and user trust** in mind.
""")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("""
<div class="footer">
🚀 Built for real-world impact | AIRWISE © 2025
</div>
""", unsafe_allow_html=True)
