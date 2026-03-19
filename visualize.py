import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    df = pd.read_csv("weather_data.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by="timestamp")

    plt.figure(figsize=(10,5))
    plt.plot(df["timestamp"], df["temperature"], marker='o')

    plt.plot(df["timestamp"], df["humidity"], marker='x')
    plt.legend(["Temperature", "Humidity"])

    plt.title("Temperature Trend Over Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_data()