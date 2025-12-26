import pandas as pd
import xgboost as xgb
import joblib

MODEL_PATH = "models/health_risk.pkl"
DATA_PATH = "data/health_risk_synthetic.csv"

def train_health_risk_model():
    df = pd.read_csv(DATA_PATH)

    X = df[["aqi", "age", "condition"]]
    y = df["risk"]

    model = xgb.XGBRegressor(
        n_estimators=300,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42
    )

    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model


def load_health_risk_model():
    return joblib.load(MODEL_PATH)