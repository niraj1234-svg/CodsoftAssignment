import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = length_slider.get()
    characters = ""

    if var_letters.get():
        characters += string.ascii_letters
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Selection Error", "Please select at least one option (letters, numbers, symbols).")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x400")
root.configure(bg="#f4f9f9")

title = tk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"), bg="#f4f9f9", fg="#34495e")
title.pack(pady=20)

length_label = tk.Label(root, text="Select Password Length:", font=("Arial", 12), bg="#f4f9f9", fg="#2c3e50")
length_label.pack()

length_slider = tk.Scale(root, from_=6, to=32, orient=tk.HORIZONTAL, length=300, bg="#f4f9f9", troughcolor="#dfe6e9", fg="#2c3e50")
length_slider.set(12)
length_slider.pack(pady=10)

var_letters = tk.IntVar(value=1)
var_numbers = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=1)

frame = tk.Frame(root, bg="#f4f9f9")
frame.pack()

tk.Checkbutton(frame, text="Letters (A-Z)", variable=var_letters, bg="#f4f9f9", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(frame, text="Numbers (0-9)", variable=var_numbers, bg="#f4f9f9", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(frame, text="Symbols (!@#)", variable=var_symbols, bg="#f4f9f9", font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=10)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 13, "bold"),
                         bg="#00b894", fg="white", activebackground="#00cec9", activeforeground="white", pady=8)
generate_btn.pack(pady=20)

# Output field
password_entry = tk.Entry(root, font=("Arial", 14), width=30, justify="center", bd=2, relief=tk.GROOVE)
password_entry.pack(pady=10)
password_entry.config(state="readonly")

root.mainloop()
