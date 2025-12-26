from xgboost import XGBRegressor

FEATURES = [
    "aqi_lag_1",
    "aqi_lag_3",
    "aqi_lag_6",
    "aqi_roll_3",
    "aqi_roll_6",
    "hour",
    "dayofweek",
    "wind",
    "humidity"
]

def train_model(df):
    X = df[FEATURES]
    y = df["aqi"]

    model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42
    )

    model.fit(X, y)
    return model
