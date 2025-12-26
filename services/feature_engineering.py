import pandas as pd


def build_features(df: pd.DataFrame, weather: dict | None = None) -> pd.DataFrame:
    """
    Build time-series features for AQI forecasting
    Expects df with index=datetime and column 'aqi'
    """

    df = df.copy()

    # -------------------------
    # Time features
    # -------------------------
    df["hour"] = df.index.hour
    df["dayofweek"] = df.index.dayofweek

    # -------------------------
    # Lag features
    # -------------------------
    df["aqi_lag_1"] = df["aqi"].shift(1)
    df["aqi_lag_3"] = df["aqi"].shift(3)
    df["aqi_lag_6"] = df["aqi"].shift(6)

    # -------------------------
    # Rolling features
    # -------------------------
    df["aqi_roll_3"] = df["aqi"].rolling(3).mean()
    df["aqi_roll_6"] = df["aqi"].rolling(6).mean()

    # -------------------------
    # Weather features (constant)
    # -------------------------
    if weather:
        df["wind"] = weather.get("wind", 0)
        df["humidity"] = weather.get("humidity", 0)
    else:
        df["wind"] = 0
        df["humidity"] = 0

    # Drop rows with NaNs from lags
    df = df.dropna()

    return df