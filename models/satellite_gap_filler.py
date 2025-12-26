def predict_aqi_no_sensor(aod, weather_factor):
    return aod * 120 + weather_factor * 10
