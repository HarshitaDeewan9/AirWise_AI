def estimate_sources(pollutants: dict) -> dict:
    """
    Estimate pollution source contribution using pollutant composition.
    Returns normalized percentages.
    """

    if not pollutants:
        return {
            "Traffic": 0,
            "Industry": 0,
            "Construction/Dust": 0,
            "Residential/Biomass": 0,
            "Secondary (Ozone)": 0,
        }

    # Initialize raw scores
    scores = {
        "Traffic": 0.0,
        "Industry": 0.0,
        "Construction/Dust": 0.0,
        "Residential/Biomass": 0.0,
        "Secondary (Ozone)": 0.0,
    }

    # Mapping logic (scientifically grounded heuristics)
    if "no2" in pollutants:
        scores["Traffic"] += pollutants["no2"]["value"] * 1.2

    if "co" in pollutants:
        scores["Traffic"] += pollutants["co"]["value"] * 0.8

    if "pm25" in pollutants:
        scores["Residential/Biomass"] += pollutants["pm25"]["value"] * 1.1

    if "pm10" in pollutants:
        scores["Construction/Dust"] += pollutants["pm10"]["value"] * 1.0

    if "so2" in pollutants:
        scores["Industry"] += pollutants["so2"]["value"] * 1.3

    if "o3" in pollutants:
        scores["Secondary (Ozone)"] += pollutants["o3"]["value"] * 1.0

    # Normalize to percentages
    total = sum(scores.values())
    if total == 0:
        return scores

    return {
        k: round((v / total) * 100, 1)
        for k, v in scores.items()
    }