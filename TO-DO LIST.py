import tkinter as tk
from tkinter import messagebox


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        open("tasks.txt", "w").close()

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in task_listbox.get(0, tk.END):
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Your tasks have been saved!")

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("✨ To-Do List App")
root.geometry("400x500")
root.configure(bg="#f0f4f7")

header = tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold"), fg="#2c3e50", bg="#f0f4f7")
header.pack(pady=15)

task_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief=tk.FLAT, highlightthickness=2, highlightcolor="#2980b9")
task_entry.pack(pady=10)


task_listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=12, bg="white", bd=2, relief=tk.GROOVE, highlightthickness=0)
task_listbox.pack(pady=10)


btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

def style_button(btn, bg, fg):
    btn.configure(bg=bg, fg=fg, activebackground="#3498db", activeforeground="white", bd=0, padx=10, pady=5, font=("Arial", 11, "bold"))

btn_add = tk.Button(btn_frame, text="Add", command=add_task)
btn_del = tk.Button(btn_frame, text="Delete", command=delete_task)
btn_save = tk.Button(btn_frame, text="Save", command=save_tasks)

for b in [btn_add, btn_del, btn_save]:
    b.pack(side=tk.LEFT, padx=8)
    style_button(b, "#2980b9", "white")

load_tasks()

root.mainloop()
