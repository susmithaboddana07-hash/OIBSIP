# 🎙️ Nova – Python Voice Assistant

## Overview

Nova is a Python-based voice assistant developed as part of the **Python Programming Internship**. The assistant is designed to recognize voice commands, perform various desktop and web-based tasks, and respond using speech synthesis, providing a simple hands-free user experience.

## Features

* Voice command recognition
* Text-to-Speech responses
* Time, Date, and Day information
* Weather updates
* Wikipedia search
* Google search
* YouTube playback
* Battery, CPU, and RAM status
* Screenshot capture
* Open Windows applications (Calculator, Notepad, Paint, Command Prompt, Camera, File Explorer)
* Open websites (Google, YouTube, Gmail, GitHub, LinkedIn, Instagram, WhatsApp Web)
* Volume control
* Coin toss and dice roll
* Jokes, random facts, and motivational quotes
* Smart fallback using Wikipedia and Google Search for unknown queries

## Technologies Used

* Python 3.x

## Python Libraries Used

* SpeechRecognition
* pyttsx3
* pywhatkit
* wikipedia
* pyjokes
* psutil
* pyautogui
* requests
* randfacts
* datetime
* random
* os
* webbrowser

## Development Tools

* Visual Studio Code
* Python Virtual Environment (venv)
* Git
* GitHub

## Project Objective

The objective of this project is to build an interactive voice assistant capable of performing common desktop operations, retrieving online information, and automating everyday tasks through voice commands using Python.

## Internship

**Python Programming Internship**

## Future Enhancements

* AI-powered conversational responses
* Email and WhatsApp automation
* Reminder and alarm system
* Voice authentication
* Smart home device integration

## Author

**Susmitha B**
## Privacy

This voice assistant processes voice input using the SpeechRecognition library. Speech is converted to text through Google's Speech Recognition service. Weather information is retrieved using the OpenWeatherMap API. Emails are sent securely using SMTP with Gmail App Password authentication.

The application does not permanently store voice recordings, email content, or personal information. Screenshots and reminder data are stored only on the user's local computer during execution. Users should keep their email credentials and API keys secure and never share them publicly.