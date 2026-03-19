import pandas as pd


def get_time_window(df, mins):

    latest_time = df["timestamp"].max()
    time_threshold = latest_time - pd.Timedelta(minutes=mins)

    return df[df["timestamp"] >= time_threshold]


def overall_stats(df):

    cities = df["city"].unique()

    print("\n===== WINDOWED STATISTICS =====")

    for city in cities:
        city_data = df[df["city"] == city]

        if len(city_data) == 0:
            print(f"\n--- {city} ---")
            print("No data available")
            continue

        print(f"\n--- {city} ---")

        print("Avg Temp:", round(city_data["temperature"].mean(), 2))
        print("Max Temp:", city_data["temperature"].max())
        print("Min Temp:", city_data["temperature"].min())
        print("Avg Humidity:", round(city_data["humidity"].mean(), 2))
        print("Max Humidity:", city_data["humidity"].max())
        print("Min Humidity:", city_data["humidity"].min())


def trend_detection(df):

    cities = df["city"].unique()

    print("\n===== TREND ANALYSIS =====")

    for city in cities:
        city_data = df[df["city"] == city]

        if len(city_data) < 2:
            print(f"\n--- {city} ---")
            print("Not enough data for trend")
            continue

        print(f"\n--- {city} ---")

        start_temp = city_data["temperature"].iloc[0]
        end_temp = city_data["temperature"].iloc[-1]

        if end_temp > start_temp:
            print("Trend: Increasing 🔺")
        elif end_temp < start_temp:
            print("Trend: Decreasing 🔻")
        else:
            print("Trend: Stable ➖")