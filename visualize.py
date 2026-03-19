import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    df = pd.read_csv("weather_data.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by="timestamp")

    #Temperature plot
    plt.figure(figsize=(10,5))

    cities = df["city"].unique()
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

    cities = df["city"].unique()
    for city in cities:
        city_data = df[df["city"] == city]
        plt.plot(city_data["timestamp"], city_data["humidity"], marker='x', label=city)

    plt.title("Humidity Trends Across Cities")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.show()
    
    cities = df["city"].unique()

    for city in cities:
        city_data = df[df["city"] == city]

        print(f"\n--- {city} ---")
        print("Average Temperature:", city_data["temperature"].mean())
        print("Max Temperature:", city_data["temperature"].max())
        print("Min Temperature:", city_data["temperature"].min())
        print("Average Humidity:", city_data["humidity"].mean())
        print("Max Humidity:", city_data["humidity"].max())
        print("Min Humidity:", city_data["humidity"].min())

if __name__ == "__main__":
    plot_data()