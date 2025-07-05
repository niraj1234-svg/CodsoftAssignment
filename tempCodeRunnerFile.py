import tkinter as tk
from tkinter import messagebox
import random

options = ['Rock', 'Paper', 'Scissors']
user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score
    comp_choice = random.choice(options)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper') or \
         (user_choice == 'Paper' and comp_choice == 'Rock'):
        user_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "You Lose!"

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\n\n{result}")
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.configure(bg="#f5f5f5")

title = tk.Label(root, text="🎮 Rock Paper Scissors", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#34495e")
title.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5f5", fg="#2c3e50")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12), bg="#f5f5f5", fg="#7f8c8d")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

def create_button(name, emoji):
    return tk.Button(
        button_frame, text=f"{emoji}\n{name}", width=10, height=3,
        font=("Arial", 12, "bold"), bg="#3498db", fg="white",
        activebackground="#2980b9", activeforeground="white",
        command=lambda: play(name)
    )

btn_rock = create_button("Rock", "🪨")
btn_paper = create_button("Paper", "📄")
btn_scissors = create_button("Scissors", "✂️")

btn_rock.grid(row=0, column=0, padx=10)
btn_paper.grid(row=0, column=1, padx=10)
btn_scissors.grid(row=0, column=2, padx=10)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score: You 0 - 0 Computer")

reset_btn = tk.Button(root, text="🔁 Play Again", command=reset_game,
                      font=("Arial", 12, "bold"), bg="#e67e22", fg="white",
                      activebackground="#d35400", activeforeground="white")
reset_btn.pack(pady=30)

root.mainloop()
