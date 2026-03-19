import pandas as pd
from datetime import datetime

def process_data(raw_data):
    processed = {
        "timestamp": datetime.now(),
        "temperature": raw_data["main"]["temp"],
        "feels_like": raw_data["main"]["feels_like"],
        "humidity": raw_data["main"]["humidity"],
        "pressure": raw_data["main"]["pressure"],
        "weather": raw_data["weather"][0]["description"]
    }

    df = pd.DataFrame([processed])
    return df

