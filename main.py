from fetch_data import fetch_weather
from process_data import process_data
import os

def main():
    raw = fetch_weather()
    df = process_data(raw)
    print(df)

    file_exists = os.path.isfile("weather_data.csv")
    df = df.sort_values(by="timestamp")
    df.to_csv("weather_data.csv", mode='a', header=not file_exists, index=False)

if __name__ == "__main__":
    main()