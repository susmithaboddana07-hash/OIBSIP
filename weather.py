from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
import requests


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        return None

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    return weather, temp