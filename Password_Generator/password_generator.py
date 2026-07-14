import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():

    try:
        length = int(length_entry.get())

        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase

        if lower_var.get():
            chars += string.ascii_lowercase

        if number_var.get():
            chars += string.digits

        if symbol_var.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showerror(
                "Error",
                "Select at least one option."
            )
            return

        password = "".join(
            random.choice(chars)
            for _ in range(length)
        )

        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except:
        messagebox.showerror(
            "Error",
            "Enter a valid length."
        )


def copy_password():

    password = result_entry.get()

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied successfully."
    )


root = tk.Tk()

root.title("Password Generator")

root.geometry("500x450")

root.configure(bg="#EAF4FF")
root.resizable(False, False)


title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF"
)

title.pack(pady=20)

length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12),
    bg="#EAF4FF"
)

length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)

length_entry.pack(pady=10)

length_entry.insert(0, "12")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Uppercase Letters",
    variable=upper_var,
    bg="#EAF4FF"
).pack()

tk.Checkbutton(
    root,
    text="Lowercase Letters",
    variable=lower_var,
    bg="#EAF4FF"
).pack()

tk.Checkbutton(
    root,
    text="Numbers",
    variable=number_var,
    bg="#EAF4FF"
).pack()

tk.Checkbutton(
    root,
    text="Special Characters",
    variable=symbol_var,
    bg="#EAF4FF"
).pack()

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#1976D2",
    fg="white",
    font=("Arial", 12, "bold")
)

generate_btn.pack(pady=20)

result_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12),
    justify="center"
)

result_entry.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#43A047",
    fg="white",
    font=("Arial", 12, "bold")
)

copy_btn.pack(pady=10)

root.mainloop()

