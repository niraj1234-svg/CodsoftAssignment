import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    refresh_contacts()
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def refresh_contacts(filtered=None):
    contact_list.delete(*contact_list.get_children())
    data = filtered if filtered is not None else contacts
    for idx, c in enumerate(data):
        contact_list.insert("", "end", iid=idx, values=(c["Name"], c["Phone"], c["Email"], c["Address"]))

def search_contact():
    keyword = search_entry.get().lower()
    filtered = [c for c in contacts if keyword in c["Name"].lower() or keyword in c["Phone"]]
    refresh_contacts(filtered)

def on_select(event):
    selected = contact_list.selection()
    if not selected:
        return
    idx = int(selected[0])
    contact = contacts[idx]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact["Name"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["Phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["Email"])
    address_entry.delete(0, tk.END)
    address_entry.insert(0, contact["Address"])

def update_contact():
    selected = contact_list.selection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a contact to update.")
        return
    idx = int(selected[0])
    contacts[idx] = {
        "Name": name_entry.get(),
        "Phone": phone_entry.get(),
        "Email": email_entry.get(),
        "Address": address_entry.get()
    }
    refresh_contacts()
    clear_entries()

def delete_contact():
    selected = contact_list.selection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a contact to delete.")
        return
    idx = int(selected[0])
    del contacts[idx]
    refresh_contacts()
    clear_entries()

root = tk.Tk()
root.title("📞 Contact Book")
root.geometry("750x600")
root.configure(bg="#f0f8ff")

title = tk.Label(root, text="Contact Book", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#2c3e50")
title.pack(pady=10)

form_frame = tk.Frame(root, bg="#f0f8ff")
form_frame.pack(pady=5)


tk.Label(form_frame, text="Name", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, sticky="w", padx=10, pady=5)
name_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Phone", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, sticky="w", padx=10, pady=5)
phone_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
phone_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Email", font=("Arial", 12), bg="#f0f8ff").grid(row=2, column=0, sticky="w", padx=10, pady=5)
email_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
email_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Address", font=("Arial", 12), bg="#f0f8ff").grid(row=3, column=0, sticky="w", padx=10, pady=5)
address_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
address_entry.grid(row=3, column=1, pady=5)

btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_contact, width=12, bg="#27ae60", fg="white", font=("Arial", 11)).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_contact, width=12, bg="#2980b9", fg="white", font=("Arial", 11)).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_contact, width=12, bg="#c0392b", fg="white", font=("Arial", 11)).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_entries, width=12, bg="#8e44ad", fg="white", font=("Arial", 11)).grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root, bg="#f0f8ff")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=40)
search_entry.grid(row=0, column=0, padx=10)
tk.Button(search_frame, text="Search", command=search_contact, bg="#16a085", fg="white", font=("Arial", 11)).grid(row=0, column=1, padx=5)

columns = ("Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, width=150)
contact_list.pack(pady=10)
contact_list.bind("<<TreeviewSelect>>", on_select)

root.mainloop()
