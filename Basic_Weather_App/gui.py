from weather import get_weather, get_forecast
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# ----------------------------
# Get Weather Function
# ----------------------------
def show_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror(
            "Input Error",
            "Please enter a city name."
        )
        return

    # Get Current Weather
    result = get_weather(city)

    if "error" in result:
        messagebox.showerror(
            "Weather Error",
            result["error"]
        )
        return

    # ----------------------------
    # Weather Icon
    # ----------------------------
    try:

        icon_url = (
            f"https://openweathermap.org/img/wn/"
            f"{result['icon']}@2x.png"
        )

        response = requests.get(icon_url)

        image = Image.open(BytesIO(response.content))
        image = image.resize((100, 100))

        photo = ImageTk.PhotoImage(image)

        icon_label.config(image=photo)
        icon_label.image = photo

    except Exception:
        icon_label.config(image="")

    # ----------------------------
    # Current Weather
    # ----------------------------
    weather_text = (
        f"📍 Location : {result['city']}, {result['country']}\n\n"
        f"🌡 Temperature : {result['temperature_c']} °C\n"
        f"🌡 Temperature : {result['temperature_f']} °F\n\n"
        f"🥵 Feels Like : {result['feels_like']} °C\n\n"
        f"☁ Condition : {result['description']}\n\n"
        f"💧 Humidity : {result['humidity']} %\n\n"
        f"🌬 Wind Speed : {result['wind_speed']} m/s\n\n"
        f"📊 Pressure : {result['pressure']} hPa\n\n"
        f"👀 Visibility : {result['visibility']} km\n\n"
        f"🌅 Sunrise : {result['sunrise']}\n\n"
        f"🌇 Sunset : {result['sunset']}"
    )

    result_label.config(text=weather_text)

    # ----------------------------
    # Forecast
    # ----------------------------
    forecast = get_forecast(city)

    if "error" in forecast:
        messagebox.showerror(
            "Forecast Error",
            forecast["error"]
        )
        return

    # Hourly Forecast
    hourly_text = ""

    for item in forecast["hourly"]:

        time = item["time"][11:16]

        hourly_text += (
            f"🕒 {time}      "
            f"🌡 {item['temp']} °C      "
            f"☁ {item['description']}\n"
        )

    forecast_label.config(text=hourly_text)

    # Daily Forecast
    daily_text = ""

    for day in forecast["daily"]:

        daily_text += (
            f"📅 {day['date']}      "
            f"🌡 {day['temp']} °C      "
            f"☁ {day['description']}\n"
        )

    daily_label.config(text=daily_text)


# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()

root.title("🌤 Weather Dashboard Pro")

root.geometry("800x700")

root.configure(bg="#EAF4FF")

# ----------------------------
# Scrollable Canvas
# ----------------------------
main_canvas = tk.Canvas(
    root,
    bg="#EAF4FF",
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=main_canvas.yview
)

scrollable_frame = tk.Frame(
    main_canvas,
    bg="#EAF4FF"
)

scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(
        scrollregion=main_canvas.bbox("all")
    )
)

main_canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

main_canvas.configure(
    yscrollcommand=scrollbar.set
)

main_canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

# ----------------------------
# Title
# ----------------------------
title = tk.Label(
    scrollable_frame,
    text="🌤 Weather Dashboard Pro",
    font=("Arial", 24, "bold"),
    bg="#EAF4FF",
    fg="#1565C0"
)
title.pack(pady=15)

subtitle = tk.Label(
    scrollable_frame,
    text="Real-Time Weather using OpenWeatherMap API",
    font=("Arial", 11),
    bg="#EAF4FF",
    fg="gray"
)
subtitle.pack()

# ----------------------------
# Search Frame
# ----------------------------
search_frame = tk.Frame(
    scrollable_frame,
    bg="#EAF4FF"
)
search_frame.pack(pady=15)

city_entry = tk.Entry(
    search_frame,
    width=25,
    font=("Arial", 14),
    justify="center"
)
city_entry.grid(row=0, column=0, padx=10)

city_entry.bind(
    "<Return>",
    lambda event: show_weather()
)

weather_button = tk.Button(
    search_frame,
    text="Get Weather",
    command=show_weather,
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    width=15
)
weather_button.grid(row=0, column=1)

# ----------------------------
# Weather Icon
# ----------------------------
icon_label = tk.Label(
    scrollable_frame,
    bg="#EAF4FF"
)
icon_label.pack(pady=10)

# ----------------------------
# Current Weather Frame
# ----------------------------
weather_frame = tk.LabelFrame(
    scrollable_frame,
    text="Current Weather",
    font=("Arial", 13, "bold"),
    bg="white",
    padx=15,
    pady=15
)
weather_frame.pack(fill="x", padx=20, pady=10)

result_label = tk.Label(
    weather_frame,
    text="Search for a city to view weather.",
    bg="white",
    justify="left",
    font=("Arial", 11)
)
result_label.pack(anchor="w")

# ----------------------------
# Hourly Forecast Frame
# ----------------------------
hourly_frame = tk.LabelFrame(
    scrollable_frame,
    text="🕒 Next 6 Hours Forecast",
    font=("Arial", 13, "bold"),
    bg="white",
    padx=15,
    pady=15
)
hourly_frame.pack(fill="x", padx=20, pady=10)

forecast_label = tk.Label(
    hourly_frame,
    text="Hourly forecast will appear here.",
    bg="white",
    justify="left",
    font=("Arial", 11)
)
forecast_label.pack(anchor="w")

# ----------------------------
# Daily Forecast Frame
# ----------------------------
daily_frame = tk.LabelFrame(
    scrollable_frame,
    text="📅 5-Day Forecast",
    font=("Arial", 13, "bold"),
    bg="white",
    padx=15,
    pady=15
)
daily_frame.pack(fill="x", padx=20, pady=10)

daily_label = tk.Label(
    daily_frame,
    text="5-day forecast will appear here.",
    bg="white",
    justify="left",
    font=("Arial", 11)
)
daily_label.pack(anchor="w")

# ----------------------------
# Footer
# ----------------------------
footer = tk.Label(
    scrollable_frame,
    text="Powered by OpenWeatherMap API",
    font=("Arial", 10),
    bg="#EAF4FF",
    fg="gray"
)
footer.pack(pady=20)

# ----------------------------
# Mouse Wheel Scrolling
# ----------------------------
def _on_mousewheel(event):
    main_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )

main_canvas.bind_all(
    "<MouseWheel>",
    _on_mousewheel
)

# ----------------------------
# Run Application
# ----------------------------
root.mainloop()

