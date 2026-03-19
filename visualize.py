import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    df = pd.read_csv("weather_data.csv")

    print(df.head()) 

    plt.plot(df["temperature"])
    plt.title("Temperature Trend")
    plt.xlabel("Data Points")
    plt.ylabel("Temperature")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    plt.plot(df["timestamp"], df["temperature"])
    plt.xticks(rotation=45) 

    plt.show()

if __name__ == "__main__":
    plot_data()