import time
from fetch_data import fetch_weather
from process_data import process_data
import os

def main():
    while True:
        raw = fetch_weather()
        df = process_data(raw)

        file_exists = os.path.isfile("weather_data.csv")
        df.to_csv("weather_data.csv", mode='a', header=not file_exists, index=False)
        print("Data logged:", df)

        time.sleep(60) 

if __name__ == "__main__":
    main()