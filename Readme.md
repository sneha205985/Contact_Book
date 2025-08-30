# ** CONTACT BOOK **

A Python-based contact manager with a graphical user interface (GUI) built using Tkinter. This version features a table layout and a search popup that allows users to filter contacts by name or number.
---

##  Features

- Add new contacts
- View saved contacts
- Update existing contact details
- Delete unwanted contacts
- **Search with popup**: Type a name or phone number and instantly view matching contacts
- Automatically saves data to `contacts.txt` using file I/O
- Simple and clean interface

---

## Technologies Used

- Python 3.x
- Tkinter for GUI
- 'tsk.Treeview' for table display
- File I/O for local data storage

---

## Folder Structure

```
ContactBook/
├── contact_book_gui.py
├── README.md
└── contacts.txt (auto-created when you add your first contact)
```

---

## How to Run the App

1. Open Terminal and navigate to your project folder:
```bash
cd ~/Desktop/ContactBook
```

2. Run the Python file:
```bash
python3 contact_book_gui.py
```

> This will open the GUI window. From there, you can manage contacts easily.

---

## How Search Works

- Click the **Search** button
- A popup asks for input
- Matching results (partial or full) are shown in the table
- If nothing matches, you get a message

---

## Data Storage

Contacts are stored in `contacts.txt` in the format:
```
Name,PhoneNumber
```

---
## Author 
 
Made by SNEHA GUPTA
