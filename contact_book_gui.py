import tkinter as tk
from tkinter import messagebox

contacts = []

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts.append((name, phone))
    except FileNotFoundError:
        pass

def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, phone in contacts:
            file.write(f"{name},{phone}\n")

def update_listbox():
    listbox.delete(0, tk.END)
    for name, phone in contacts:
        listbox.insert(tk.END, f"{name} - {phone}")

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        contacts.append((name, phone))
        save_contacts()
        update_listbox()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both Name and Phone.")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        save_contacts()
        update_listbox()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

def reset_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def on_select(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        name, phone = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, phone)

def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_name = entry_name.get()
        new_phone = entry_phone.get()
        if new_name and new_phone:
            contacts[index] = (new_name, new_phone)
            save_contacts()
            update_listbox()
        else:
            messagebox.showwarning("Input Error", "Both fields required.")
    else:
        messagebox.showwarning("No Selection", "Select a contact to update.")

# GUI setup
root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Button(root, text="Add", command=add_contact).grid(row=2, column=0)
tk.Button(root, text="Update", command=update_contact).grid(row=2, column=1)
tk.Button(root, text="Delete", command=delete_contact).grid(row=3, column=0)
tk.Button(root, text="Reset", command=reset_fields).grid(row=3, column=1)

listbox = tk.Listbox(root, width=40)
listbox.grid(row=4, column=0, columnspan=2)
listbox.bind("<<ListboxSelect>>", on_select)

load_contacts()
update_listbox()

root.mainloop()
