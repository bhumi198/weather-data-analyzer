import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    df = pd.read_csv("weather_data.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by="timestamp")

    plt.figure(figsize=(10,5))
    plt.plot(df["timestamp"], df["temperature"], label="Temperature", marker='o')

    plt.plot(df["timestamp"], df["humidity"], label="Humidity", marker='x')

    # Highlight anomalies
    anomalies = df[df["alert"] != "Normal"]
    plt.scatter(anomalies["timestamp"], anomalies["temperature"], color='red', label="Anomaly")

    plt.title("Temperature & HumidityTrends with Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_data()