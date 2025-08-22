# MADE BY KAIF TARASAGAR
import tkinter as tk
from tkinter import messagebox
import json, os, re

contacts = {}# MADE BY KAIF TARASAGAR

def load_data():
    global contacts
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as f:
                data = json.load(f)
                if isinstance(data, dict):# MADE BY KAIF TARASAGAR
                    contacts = data
                elif isinstance(data, list):
                    contacts = {item['name']: {
                        "phone": item.get("phone", ""),
                        "email": item.get("email", ""),
                        "address": item.get("address", "")
                    } for item in data}
        except:
            contacts = {}

def save_data():# MADE BY KAIF TARASAGAR
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

def show_contacts():
    listbox.delete(0, tk.END)
    for name in sorted(contacts):
        listbox.insert(tk.END, name)

def clear_fields():
    for entry in (entry_name, entry_phone, entry_email, entry_address):
        entry.delete(0, tk.END)
    listbox.selection_clear(0, tk.END)

def validate_contact(name, phone, email):# MADE BY KAIF TARASAGAR
    if not name:
        messagebox.showerror("Error", "Name is required!")
        return False
    if phone and not phone.isdigit():
        messagebox.showerror("Error", "Phone must be digits only!")
        return False# MADE BY KAIF TARASAGAR
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format!")
        return False
    return True

def add_contact():# MADE BY KAIF TARASAGAR
    name, phone, email, address = get_form_data()
    if not validate_contact(name, phone, email):
        return
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_data()# MADE BY KAIF TARASAGAR
    show_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact added!")

def update_contact():
    sel = listbox.curselection()
    if not sel:
        messagebox.showerror("Error", "Select a contact to update!")
        return# MADE BY KAIF TARASAGAR
    old_name = listbox.get(sel[0])
    name, phone, email, address = get_form_data()
    if not validate_contact(name, phone, email):
        return# MADE BY KAIF TARASAGAR
    if old_name != name:
        contacts.pop(old_name, None)
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_data()
    show_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact updated!")
# MADE BY KAIF TARASAGAR
def delete_contact():
    sel = listbox.curselection()
    if not sel:
        messagebox.showerror("Error", "Select a contact to delete!")
        return
    name = listbox.get(sel[0])
    if messagebox.askyesno("Confirm", f"Delete {name}?"):
        contacts.pop(name, None)
        save_data()# MADE BY KAIF TARASAGAR
        show_contacts()
        clear_fields()

def search_contact():
    q = entry_search.get().strip().lower()
    listbox.delete(0, tk.END)
    for name in sorted(contacts):
        if q in name.lower():
            listbox.insert(tk.END, name)# MADE BY KAIF TARASAGAR

def select_contact(e):
    sel = listbox.curselection()
    if not sel:
        return# MADE BY KAIF TARASAGAR
    name = listbox.get(sel[0])
    data = contacts[name]
    entry_name.delete(0, tk.END)
    entry_name.insert(0, name)
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, data["phone"])# MADE BY KAIF TARASAGAR
    entry_email.delete(0, tk.END)
    entry_email.insert(0, data["email"])
    entry_address.delete(0, tk.END)
    entry_address.insert(0, data["address"])

def get_form_data():
    return (
        entry_name.get().strip(),
        entry_phone.get().strip(),
        entry_email.get().strip(),
        entry_address.get().strip()
    )# MADE BY KAIF TARASAGAR

root = tk.Tk()
root.title("Contact Book")
root.geometry("700x400")
root.resizable(False, False)

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

entry_search = tk.Entry(frame_left)
entry_search.pack(fill=tk.X, pady=5)
tk.Button(frame_left, text="Search", command=search_contact).pack(fill=tk.X)
# MADE BY KAIF TARASAGAR
listbox = tk.Listbox(frame_left, height=20)
listbox.pack(fill=tk.BOTH, expand=True, pady=5)
listbox.bind("<<ListboxSelect>>", select_contact)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

labels = ["Name:", "Phone:", "Email:", "Address:"]
entries = []# MADE BY KAIF TARASAGAR
for i, label in enumerate(labels):
    tk.Label(frame_right, text=label).grid(row=i, column=0, sticky="w")
    e = tk.Entry(frame_right)
    e.grid(row=i, column=1, pady=2, sticky="ew")
    entries.append(e)

entry_name, entry_phone, entry_email, entry_address = entries

frame_btns = tk.Frame(frame_right)
frame_btns.grid(row=4, column=0, columnspan=2, pady=10)

btn_data = [# MADE BY KAIF TARASAGAR
    ("Add", add_contact),
    ("Update", update_contact),
    ("Delete", delete_contact),
    ("Clear", clear_fields)
]
for i, (text, cmd) in enumerate(btn_data):
    tk.Button(frame_btns, text=text, command=cmd).grid(row=0, column=i, padx=5)
# MADE BY KAIF TARASAGAR
frame_right.columnconfigure(1, weight=1)

load_data()
show_contacts()
root.mainloop()# MADE BY KAIF TARASAGAR



                                        #-- MADE BY KAIF TARASAGAR 
                                               
                                         # https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                         # https://x.com/Kaif_T_200