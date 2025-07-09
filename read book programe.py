import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

contacts = {}  # Dictionary to store contacts

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

# View contact list
def view_contacts():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {info['phone']}")

# Search contact
def search_contact():
    query = search_entry.get()
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['phone']:
            contact_listbox.insert(tk.END, f"{name} - {info['phone']}")

# Update contact
def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = {
            'phone': phone_entry.get(),
            'email': email_entry.get(),
            'address': address_entry.get()
        }
        messagebox.showinfo("Updated", "Contact updated successfully.")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Not Found", "Contact does not exist.")

# Delete contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", "Contact deleted successfully.")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Not Found", "Contact does not exist.")

# Load selected contact to fields
def load_contact(event):
    selection = contact_listbox.get(contact_listbox.curselection())
    name = selection.split(" - ")[0]
    if name in contacts:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contacts[name]['phone'])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, contacts[name]['email'])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, contacts[name]['address'])

# Clear all input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Input Fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=2)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=2)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=2)

# Search
tk.Label(root, text="Search").pack()
search_entry = tk.Entry(root)
search_entry.pack()
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=2)

# Contact List
tk.Label(root, text="Contact List").pack()
contact_listbox = tk.Listbox(root)
contact_listbox.pack(fill=tk.BOTH, expand=True)
contact_listbox.bind('<<ListboxSelect>>', load_contact)

view_contacts()

root.mainloop()
