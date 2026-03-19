import pandas as pd
import matplotlib.pyplot as plt
from analysis import overall_stats, get_time_window, trend_detection

def plot_data():

    df = pd.read_csv("weather_data.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by="timestamp")

    try:
        n_mins = int(input("\nEnter time window (in minutes) for analysis: "))
    except:
        print("Invalid input. Using default = 5 minutes.")
        n_mins = 5
    df = get_time_window(df, n_mins)

    cities = df["city"].unique()

    #Temperature plot
    plt.figure(figsize=(10,5))
   
    for city in cities:
        city_data = df[df["city"] == city]
        plt.plot(city_data["timestamp"], city_data["temperature"], marker='o', label=city)

    # Highlight anomalies
    anomalies = df[df["alert"] != "Normal"]
    plt.scatter(anomalies["timestamp"], anomalies["temperature"], color='red', label="Anomaly")

    plt.title("Temperature Trends Across Cities")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    #Humidity plot
    plt.figure(figsize=(10,5))

    for city in cities:
        city_data = df[df["city"] == city]
        plt.plot(city_data["timestamp"], city_data["humidity"], marker='x', label=city)

    plt.title("Humidity Trends Across Cities")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    #Stats
    overall_stats(df)
    trend_detection(df)

    plt.show()

if __name__ == "__main__":
    plot_data()