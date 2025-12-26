from models.health_risk_model import load_health_risk_model

_model = load_health_risk_model()

def health_risk_score(aqi, age, condition):
    return int(
        min(
            _model.predict([[aqi, age, condition]])[0],
            100
        )
    )