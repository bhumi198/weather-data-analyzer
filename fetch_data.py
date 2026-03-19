import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")      
CITIES = ["Mumbai", "Delhi", "Bangalore"]

def fetch_weather():
    
    alldata=[]
    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        data["city"] = city
        alldata.append(data)

    return alldata

if __name__ == "__main__":
    print(fetch_weather())