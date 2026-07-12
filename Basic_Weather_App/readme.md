# 🌤 Weather APP

A Python desktop weather application built using **Tkinter** and the **OpenWeatherMap API**. The application provides real-time weather information, weather icons, hourly forecasts, and a 5-day forecast through a clean and user-friendly graphical interface.

---

## 📌 Features

- 🔍 Search weather by city name
- 🌡 Display temperature in Celsius and Fahrenheit
- 🥵 Feels like temperature
- 💧 Humidity
- 🌬 Wind speed
- 📊 Atmospheric pressure
- 👀 Visibility
- ☁ Current weather condition
- 🌅 Sunrise and Sunset timings
- 🖼 Weather icons
- 🕒 Next 6-hour weather forecast
- 📅 5-day weather forecast
- ❌ Error handling for:
  - Empty city input
  - Invalid city name
  - Invalid API key
  - Network errors
- 🖥 Professional Tkinter GUI
- 📜 Scrollable dashboard

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- Requests
- Pillow (PIL)
- OpenWeatherMap API

---

## 📂 Project Structure

```
Weather-App/
│
├── gui.py
├── weather.py
├── config.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-dashboard-pro.git
```

### 2. Open the project

```bash
cd weather-dashboard-pro
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get an OpenWeatherMap API Key

- Create a free account at https://openweathermap.org/
- Generate an API key.
- Open `config.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

### 5. Run the application

```bash
python gui.py
```

---

## 📷 Screenshots

Add screenshots of your application here.

Example:

- Home Screen
- Current Weather
- Hourly Forecast
- 5-Day Forecast

---

## 📖 How It Works

1. Enter a city name.
2. Click **Get Weather**.
3. The application retrieves real-time weather information using the OpenWeatherMap API.
4. Current weather details, weather icon, next 6-hour forecast, and 5-day forecast are displayed.

---

## 📌 API Used

OpenWeatherMap API

https://openweathermap.org/api

---

## 📄 Requirements

```
requests
Pillow
```

Install them using:

```bash
pip install requests pillow
```

---

## 🎯 Future Improvements

- Automatic location detection
- Dark mode
- Weather alerts
- Air Quality Index (AQI)
- Weather history
- Theme customization

---

## 👩‍💻 Developed By

**Susmitha B**

B.Tech – Computer Science & Engineering (AI)

Python Developer | AI & Machine Learning Enthusiast

---

## 📜 License

This project is created for educational and internship purposes.