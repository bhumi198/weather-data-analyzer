# 🌦️ Weather Data Analyzer

A Python-based data pipeline that fetches, processes, and analyzes real-time weather data across multiple cities with time-window based insights.

---

##  Features

-  Fetches live weather data using API  
-  Processes and structures raw JSON data  
-  Visualizes temperature and humidity trends  
-  Detects anomalies in temperature  
-  Performs **time-window based analysis (last n minutes)**  
-  Identifies trends (increasing / decreasing / stable)  
-  Supports multi-city analysis  

---

##  Project Architecture
- fetch_data.py → Fetch weather data from API
- process_data.py → Clean and structure data
- main.py → Continuous data logging
- analysis.py → Statistical & trend analysis
- visualize.py → Plotting and visualization

---

##  How It Works

1. `main.py` continuously collects weather data and stores it in `weather_data.csv`  
2. `visualize.py`:
   - Takes user input for time window (in minutes)  
   - Filters data for the selected time window  
   - Generates plots and performs analysis  

---

##  Analysis Performed

- Temperature & Humidity trends  
- Anomaly detection (threshold-based)  
- Time-window statistics (avg, max, min)  
- Trend detection based on recent data  

---

##  Technologies Used

- Python  
- Pandas  
- Matplotlib  
- REST API (weather data)  

---

##  How to Run

### 1. Clone the repository
- git clone https://github.com/bhumi198/weather-data-analyzer.git
- cd weather-data-analyzer

### 2. Create virtual environment
- python -m venv venv
- venv\Scripts\activate

### 3. Install dependencies
- pip install -r requirements.txt

### 4. Run data collection
- python main.py

### 5. Run visualization & analysis
- python visualize.py
  
---

## 📌 Notes

- Data is stored locally in `weather_data.csv`  
- Time-window analysis ensures relevant and recent insights  
- Some project components simulate real-time data pipelines  

---

## 🌌 Future Improvements

- Real-time dashboard (Streamlit)  
- Advanced anomaly detection (statistical models)  
- Database integration (PostgreSQL / MongoDB)  
- Deployment as a web application  

---
