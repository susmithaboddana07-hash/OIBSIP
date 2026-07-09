import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import wikipedia
import pyjokes
import psutil
import pyautogui
import requests
import random
import threading
import time
import os

import smtplib
from email.message import EmailMessage

try:
    import randfacts
    HAS_RANDFACTS = True
except ImportError:
    HAS_RANDFACTS = False

# ==========================
# SETTINGS
# ==========================

WEATHER_API_KEY = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
import requests


assistant_name = "Nova"
user_name = ""

# ==========================
# SEND EMAIL
# ==========================

    
            

# ==========================
# EMAIL SETTINGS
# ==========================

EMAIL_ADDRESS = "susmitha123@gmail.com"
EMAIL_PASSWORD = "abcd efgh mnop"

# ==========================
# SEND EMAIL
# ==========================

def send_email(receiver_email, subject, message):

    try:

        email = EmailMessage()

        email["From"] = EMAIL_ADDRESS
        email["To"] = receiver_email
        email["Subject"] = subject

        email.set_content(message)

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(email)

        return True

    except Exception as e:

        print(e)
        return False
    


        





# ==========================
# TEXT TO SPEECH
# ==========================

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ==========================
# SPEECH RECOGNITION
# ==========================

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            speak("Internet connection problem.")
            return ""

        except Exception:
            return ""
        

        # ==========================
# NATURAL LANGUAGE
# ==========================

def normalize_command(command):

    command = command.lower()

    remove_words = [
        "could you",
        "can you",
        "would you",
        "please",
        "tell me",
        "show me",
        "i want to",
        "i would like to",
        "for me",
        "hey nova",
        "nova"
    ]

    for word in remove_words:
        command = command.replace(word, "")

    return command.strip()
        

        # ==========================
# REMINDER
# ==========================

def set_reminder(seconds, message):

    def reminder():

        time.sleep(seconds)

        speak(f"Reminder. {message}")

    threading.Thread(target=reminder, daemon=True).start()
        



        

        # ==========================
# SEND EMAIL
# ==========================


# ==========================
# GREETING
# ==========================

def wish():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Nova Assistant is ready.")

# ==========================
# MOTIVATION QUOTES
# ==========================

motivation_quotes = [

    "Believe in yourself.",

    "Keep learning every day.",

    "Success comes through consistency.",

    "Dream big and work hard.",

    "Every expert was once a beginner."

]

thanks_reply = [

    "You're welcome.",

    "Happy to help.",

    "Anytime.",

    "My pleasure."

]

# ==========================
# WEATHER
# ==========================

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:

        response = requests.get(url)

        data = response.json()

        if str(data["cod"]) == "200":

            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            feels_like = data["main"]["feels_like"]

            return weather, temp, humidity, feels_like

        else:
            return None

    except:
        return None


# ==========================
# BATTERY
# ==========================

def battery_status():

    battery = psutil.sensors_battery()

    if battery:

        return f"Battery percentage is {battery.percent} percent."

    return "Battery information is unavailable."


# ==========================
# CPU USAGE
# ==========================

def cpu_usage():

    cpu = psutil.cpu_percent(interval=1)

    return f"CPU usage is {cpu} percent."


# ==========================
# RAM USAGE
# ==========================

def ram_usage():

    ram = psutil.virtual_memory()

    return f"RAM usage is {ram.percent} percent."


# ==========================
# SCREENSHOT
# ==========================

def take_screenshot():

    filename = "screenshot_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    image = pyautogui.screenshot()

    image.save(filename)

    return filename


# ==========================
# COIN TOSS
# ==========================

def flip_coin():

    return random.choice(["Heads", "Tails"])


# ==========================
# DICE
# ==========================

def roll_dice():

    return random.randint(1, 6)
# ==========================
# MAIN ASSISTANT
# ==========================

def run():

    global user_name

    wish()

    while True:

      command = listen()

      if command == "":
        continue

      command = normalize_command(command)    


      print("DEBUG:", command)

        # EXIT
      if any(word in command for word in ["exit", "quit", "bye", "stop"]):

            speak("Goodbye. Have a nice day.")

            break

        # GREETINGS
      elif any(word in command for word in ["hello", "hi", "hey"]):

            speak("Hello! How can I help you?")

      elif "how are you" in command:
            speak("I am doing great. Thank you for asking.")

      elif "who are you" in command:

            speak("I am Nova, your Python voice assistant.")

      elif "who created you" in command:

            speak("I was created by Susmitha.")

        # REMEMBER NAME
      elif "my name is" in command:

            user_name = command.replace("my name is", "").strip()

            speak(f"Nice to meet you {user_name}")

      elif "what is my name" in command:

            if user_name:

                speak(f"Your name is {user_name}")

            else:

                speak("I don't know your name yet.")

        # TIME
      elif "time" in command:

            current = datetime.datetime.now().strftime("%I:%M %p")

            speak(f"The time is {current}")

        # DATE
      elif "date" in command:

            today = datetime.datetime.now().strftime("%d %B %Y")

            speak(f"Today is {today}")

        # DAY
      elif "day" in command:

            today = datetime.datetime.now().strftime("%A")

            speak(f"Today is {today}")

        # JOKE
      elif "joke" in command:

            speak(pyjokes.get_joke())

        # FACT
      elif "fact" in command:

            if HAS_RANDFACTS:

                speak(randfacts.get_fact())

            else:

                speak("Python is one of the world's most popular programming languages.")

        # MOTIVATION
      elif "motivate me" in command or "motivation" in command:

            speak(random.choice(motivation_quotes))

        # THANKS
      elif "thank you" in command or "thanks" in command:

            speak(random.choice(thanks_reply))

                 # ==========================
        # WEATHER
        # ==========================

      elif "weather" in command:

            speak("Which city?")

            city = listen()



            if city:

                result = get_weather(city)

                if result:

                    weather, temp, humidity, feels = result

                    speak(
                        f"The weather in {city} is {weather}. "
                        f"The temperature is {temp} degree Celsius. "
                        f"Humidity is {humidity} percent. "
                        f"It feels like {feels} degree Celsius."
                    )

                else:

                    speak("Sorry, I couldn't get the weather.")

            else:

                speak("I didn't hear the city name.")

        # ==========================
        # GOOGLE SEARCH
        # ==========================

      elif "search" in command:

            topic = command.replace("search", "").strip()

            if topic:

                speak(f"Searching Google for {topic}")

                pywhatkit.search(topic)

            else:

                speak("Please tell me what to search.")

        # ==========================
        # PLAY ON YOUTUBE
        # ==========================

      elif "play" in command:

            song = command.replace("play", "").strip()

            if song:

                speak(f"Playing {song} on YouTube.")

                pywhatkit.playonyt(song)

            else:

                speak("Please tell me the song name.")

        # ==========================
        # WIKIPEDIA
        # ==========================

      elif "wikipedia" in command:

            topic = command.replace("wikipedia", "").strip()

            try:

                result = wikipedia.summary(topic, sentences=2)

                speak(result)

            except:

                speak("Sorry, I couldn't find anything on Wikipedia.")

        # ==========================
        # OPEN WEBSITES
        # ==========================

      elif "open google" in command:

            speak("Opening Google.")

            webbrowser.open("https://www.google.com")

      elif "open youtube" in command:

            speak("Opening YouTube.")

            webbrowser.open("https://www.youtube.com")

      elif "open gmail" in command:

            speak("Opening Gmail.")

            webbrowser.open("https://mail.google.com")

      elif "open github" in command:

            speak("Opening GitHub.")

            webbrowser.open("https://github.com")

      elif "open linkedin" in command:

            speak("Opening LinkedIn.")

            webbrowser.open("https://www.linkedin.com")

      elif "open instagram" in command:

            speak("Opening Instagram.")

            webbrowser.open("https://www.instagram.com")

      elif "open whatsapp" in command:

            speak("Opening WhatsApp Web.")

            webbrowser.open("https://web.whatsapp.com")   

                # ==========================
        # BATTERY
        # ==========================

      elif "battery" in command:

            speak(battery_status())

        # ==========================
        # CPU USAGE
        # ==========================

      elif "cpu" in command or "cpu usage" in command:

            speak(cpu_usage())

        # ==========================
        # RAM USAGE
        # ==========================

      elif "ram" in command or "memory usage" in command:

            speak(ram_usage())

        # ==========================
        # SCREENSHOT
        # ==========================

      elif "screenshot" in command:

            filename = take_screenshot()

            speak(f"Screenshot saved as {filename}")

        # ==========================
        # OPEN WINDOWS APPS
        # ==========================

      elif "open calculator" in command:

            speak("Opening Calculator.")

            os.system("calc")

      elif "open notepad" in command:

            speak("Opening Notepad.")

            os.system("notepad")

      elif "open paint" in command:

            speak("Opening Paint.")

            os.system("mspaint")

      elif "open command prompt" in command:

            speak("Opening Command Prompt.")

            os.system("start cmd")

      elif "open file explorer" in command:

            speak("Opening File Explorer.")

            os.system("explorer")

      elif "open camera" in command:

            speak("Opening Camera.")

            os.system("start microsoft.windows.camera:")

        # ==========================
        # VOLUME CONTROL
        # ==========================

      elif "volume up" in command:

            pyautogui.press("volumeup")

            speak("Volume increased.")

      elif "volume down" in command:

            pyautogui.press("volumedown")

            speak("Volume decreased.")

      elif "mute" in command:

            pyautogui.press("volumemute")

            speak("Volume muted.")

        # ==========================
        # COIN TOSS
        # ==========================

      elif "flip a coin" in command:

            speak(f"It is {flip_coin()}.")

        # ==========================
        # DICE
        # ==========================

      elif "roll dice" in command or "roll a dice" in command:

            speak(f"You rolled {roll_dice()}.") 

                # ==========================
        # SEND EMAIL
        # ==========================

      elif "send email" in command:

            speak("Please say the recipient email address.")

            receiver_email = listen().replace(" ", "").lower()

            speak("What is the subject?")

            subject = listen()

            speak("What is the message?")

            message = listen()

            if receiver_email and subject and message:

                if send_email(receiver_email, subject, message):

                    speak("Email sent successfully.")

                else:

                    speak("Sorry, I could not send the email.")

            else:

                speak("Email cancelled.")  


                # ==========================
# REMINDER
# ==========================

      elif "remind me" in command:

            try:

                speak("How many seconds from now?")

                number = listen()

                numbers = {
                  "one": 1,
                  "two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9,
                  "ten": 10,
                  "fifteen": 15,
                  "twenty": 20,
                  "thirty": 30,
                  "sixty": 60
                }

                if number.isdigit():
                    seconds = int(number)
                else:
                    seconds = numbers.get(number.lower(), 10)

                speak("What should I remind you about?")

                reminder_text = listen()

                set_reminder(seconds, reminder_text)

                speak(f"Reminder set for {seconds} seconds.")

            except:

                speak("Sorry, I couldn't set the reminder.")  



                 # ==========================
        # SMART QUESTION ANSWERING
        # ==========================

      else:

            topic = command

            # Remove common question words
            for word in [
                "what is",
                "who is",
                "what are",
                "who are",
                "tell me about",
                "explain",
                "define",
                "describe",
                "information about",
                "can you explain",
                "give me information about"
            ]:

                topic = topic.replace(word, "")

            topic = topic.replace("?", "").strip()

            try:

                speak("Let me check.")

                answer = wikipedia.summary(topic, sentences=2)

                speak(answer)

            except:

                speak("I couldn't find an exact answer. Opening Google search.")

                pywhatkit.search(topic)


                # ==========================
 

        


# ==========================
# START PROGRAM
# ==========================

if __name__ == "__main__":

    run()       
            