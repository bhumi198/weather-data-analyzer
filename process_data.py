import pandas as pd
from datetime import datetime

def detect_anomaly(temp):
    if temp > 35:
        return "High Temperature Alert"
    elif temp < 10:
        return "Low Temperature Alert"
    else:
        return "Normal"

def process_data(raw_data):
    processed = {
        "timestamp": datetime.now(),
        "temperature": raw_data["main"]["temp"],
        "feels_like": raw_data["main"]["feels_like"],
        "humidity": raw_data["main"]["humidity"],
        "pressure": raw_data["main"]["pressure"],
        "weather": raw_data["weather"][0]["description"],
        "alert": detect_anomaly(raw_data["main"]["temp"])
    }

    df = pd.DataFrame([processed])
    return df
