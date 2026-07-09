import threading
from assistant import start_assistant

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

window = tk.Tk()
window.title("AI Voice Assistant")
window.geometry("700x500")

title = tk.Label(
    window,
    text="🎙 AI Voice Assistant",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

chat = ScrolledText(window, width=70, height=20)
chat.pack(pady=10)

status = tk.Label(
    window,
    text="Status : Ready",
    font=("Arial", 12)
)
status.pack()

def start():
    status.config(text="Status : Listening...")
    chat.insert(tk.END, "Assistant started...\n")

    thread = threading.Thread(target=start_assistant)
    thread.daemon = True
    thread.start()

def stop():
    status.config(text="Status : Stopped")
    chat.insert(tk.END, "Assistant: Stopped.\n")

start_button = tk.Button(
    window,
    text="🎤 Start",
    width=20,
    command=start
)

stop_button = tk.Button(
    window,
    text="⛔ Stop",
    width=20,
    command=stop
)

start_button.pack(pady=10)
stop_button.pack()

window.mainloop()