import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# Synthetic training dataset
# -----------------------------
data = []

np.random.seed(42)

for _ in range(5000):
    aqi = np.random.randint(20, 400)
    age = np.random.randint(1, 90)
    condition = np.random.choice([0, 1], p=[0.7, 0.3])

    risk = (
        aqi * 0.25
        + age * 0.3
        + condition * 30
        + np.random.normal(0, 5)
    )

    risk = max(0, min(100, risk))

    data.append([aqi, age, condition, risk])

df = pd.DataFrame(
    data,
    columns=["aqi", "age", "condition", "risk"]
)

# -----------------------------
# Train model
# -----------------------------
X = df[["aqi", "age", "condition"]]
y = df["risk"]

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# Save model
# -----------------------------
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "health_risk.pkl"
)

joblib.dump(model, MODEL_PATH)

print("✅ Health risk model trained and saved at:", MODEL_PATH)
