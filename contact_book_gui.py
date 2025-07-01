import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

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
    tree.delete(*tree.get_children())
    for name, phone in contacts:
        tree.insert("", "end", values=(name, phone))

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
    selected = tree.selection()
    if selected:
        index = tree.index(selected[0])
        contacts.pop(index)
        save_contacts()
        update_listbox()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

def reset_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def on_select(event):
    selected = tree.selection()
    if selected:
        name, phone = tree.item(selected[0])["values"]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, phone)

def update_contact():
    selected = tree.selection()
    if selected:
        index = tree.index(selected[0])
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

def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or number to search:")
    if search_term:
        search_term = search_term.lower()
        tree.delete(*tree.get_children())
        found = False
        for name, phone in contacts:
            if search_term in name.lower() or search_term in phone:
                tree.insert("", "end", values=(name, phone))
                found = True
        if not found:
            messagebox.showinfo("Search Result", "No matching contact found.")
    else:
        messagebox.showinfo("Cancelled", "Search cancelled.")

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
tk.Button(root, text="Search", command=search_contact).grid(row=2, column=2)

# Treeview Table
tree = ttk.Treeview(root, columns=("Name", "Phone"), show="headings", height=8)
tree.heading("Name", text="Name")
tree.heading("Phone", text="Contact Number")
tree.grid(row=5, column=0, columnspan=3, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=5, column=3, sticky="ns")

load_contacts()
update_listbox()

root.mainloop()
