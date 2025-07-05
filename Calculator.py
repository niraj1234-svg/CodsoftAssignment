import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator")

text_result = tk.Text(root, height=2, width=25, font=("Arial", 18))
text_result.grid(columnspan=4)

buttons = [
    ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("%", 5, 2), ("=", 5, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, command=evaluate_calculation, width=5, height=2, font=("Arial", 14), bg="#4CAF50", fg="white")
    elif text == "C":
        btn = tk.Button(root, text=text, command=clear_field, width=5, height=2, font=("Arial", 14), bg="#f44336", fg="white")
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, height=2, font=("Arial", 14))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
