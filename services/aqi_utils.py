def openweather_to_us_aqi(ow_aqi: int) -> int:
    """
    Convert OpenWeather AQI (1–5) → approximate US AQI (0–500)
    """
    mapping = {
        1: 50,
        2: 100,
        3: 150,
        4: 200,
        5: 300
    }
    return mapping.get(int(ow_aqi), 100)
