import requests
from config import API_KEY, BASE_URL, FORECAST_URL
from datetime import datetime


def get_weather(city):
    """
    Fetch current weather data.
    """

    if not city.strip():
        return {"error": "City name cannot be empty."}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code == 401:
            return {"error": "Invalid API key."}

        if response.status_code == 404:
            return {"error": "City not found."}

        if response.status_code != 200:
            return {"error": data.get("message", "Something went wrong.")}

        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature_c": data["main"]["temp"],
            "temperature_f": round((data["main"]["temp"] * 9 / 5) + 32, 2),
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"],
            "wind_speed": data["wind"]["speed"],
            "visibility": data.get("visibility", 0) / 1000,
            "sunrise": datetime.fromtimestamp(
                data["sys"]["sunrise"]
            ).strftime("%I:%M %p"),
            "sunset": datetime.fromtimestamp(
                data["sys"]["sunset"]
            ).strftime("%I:%M %p"),
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"]
        }

        return weather

    except requests.exceptions.Timeout:
        return {"error": "Request timed out."}

    except requests.exceptions.ConnectionError:
        return {"error": "No internet connection."}

    except Exception as e:
        return {"error": str(e)}


def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            FORECAST_URL,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:
            return {"error": data.get("message")}

        hourly = []
        daily = []
        added_dates = set()

        for item in data["list"]:

            # Hourly forecast (first 6 entries)
            if len(hourly) < 6:
                hourly.append({
                    "time": item["dt_txt"],
                    "temp": item["main"]["temp"],
                    "description": item["weather"][0]["description"].title(),
                    "icon": item["weather"][0]["icon"]
                })

            # Daily forecast (one entry per day)
            date = item["dt_txt"].split()[0]

            if date not in added_dates:
                added_dates.add(date)

                daily.append({
                    "date": date,
                    "temp": item["main"]["temp"],
                    "description": item["weather"][0]["description"].title(),
                    "icon": item["weather"][0]["icon"]
                })

            if len(daily) == 5:
                break

        return {
            "hourly": hourly,
            "daily": daily
        }

    except requests.exceptions.Timeout:
        return {"error": "Request timed out."}

    except requests.exceptions.ConnectionError:
        return {"error": "No internet connection."}

    except Exception as e:
        return {"error": str(e)}