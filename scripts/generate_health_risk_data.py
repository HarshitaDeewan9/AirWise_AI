# scripts/generate_health_risk_data.py
import pandas as pd
import random

rows = []

for _ in range(5000):
    aqi = random.randint(20, 500)
    age = random.randint(5, 90)
    condition = random.choice([0, 1])

    risk = (
        aqi * 0.25 +
        age * 0.3 +
        (25 if condition else 0) +
        random.randint(-5, 5)
    )

    risk = max(0, min(int(risk), 100))
    rows.append([aqi, age, condition, risk])

df = pd.DataFrame(rows, columns=["aqi", "age", "condition", "risk"])
df.to_csv("data/health_risk_synthetic.csv", index=False)

print("✅ Synthetic health risk dataset created")