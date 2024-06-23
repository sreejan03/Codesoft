import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Password length must be at least 1")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

# Set up the main window
root = tk.Tk()
root.title("Password Generator")

# Set up the input label and entry
tk.Label(root, text="Enter password length:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Set up the generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Set up the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()