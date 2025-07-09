import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Length must be at least 4")

        chars = ""
        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("Selection Error", "Select at least one character type!")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        output_entry.delete(0, tk.END)
        output_entry.insert(0, password)

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# Copy password to clipboard
def copy_to_clipboard():
    generated = output_entry.get()
    if generated:
        root.clipboard_clear()
        root.clipboard_append(generated)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main window
root = tk.Tk()
root.title("Professional Password Generator")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

# Length input
frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=5)
tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="#f2f2f2").pack(side="left")
length_entry = tk.Entry(frame, width=5, font=("Arial", 12))
length_entry.insert(0, "12")
length_entry.pack(side="left", padx=10)

# Options
option_frame = tk.LabelFrame(root, text="Include Characters", font=("Arial", 10, "bold"), bg="#f2f2f2")
option_frame.pack(padx=20, pady=10, fill="both")

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(option_frame, text="Uppercase (A-Z)", variable=var_upper, bg="#f2f2f2").pack(anchor="w")
tk.Checkbutton(option_frame, text="Lowercase (a-z)", variable=var_lower, bg="#f2f2f2").pack(anchor="w")
tk.Checkbutton(option_frame, text="Digits (0-9)", variable=var_digits, bg="#f2f2f2").pack(anchor="w")
tk.Checkbutton(option_frame, text="Symbols (!@#)", variable=var_symbols, bg="#f2f2f2").pack(anchor="w")

# Output field
output_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
output_entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Generate", font=("Arial", 11), bg="#4CAF50", fg="white", command=generate_password).pack(side="left", padx=10)
tk.Button(btn_frame, text="Copy", font=("Arial", 11), bg="#2196F3", fg="white", command=copy_to_clipboard).pack(side="left", padx=10)

root.mainloop()
