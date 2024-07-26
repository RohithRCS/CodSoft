import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(event=None):
    try:
        length=int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error","Please enter a positive number.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        label_password.config(text=f"Generated password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def copy_to_clipboard():
    password = label_password.cget("text").replace("Generated password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

large_font = ("Helvetica", 14)

label_length = tk.Label(root, text="Enter password length:", font=large_font)
label_length.pack(pady=5)

entry_length = tk.Entry(root, width=30, font=large_font)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password, font=large_font, bg="lightblue", fg="black")
button_generate.pack(pady=10)

label_password = tk.Label(root, text="", font=large_font)
label_password.pack(pady=15)

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=large_font, bg="lightgreen", fg="black")
button_copy.pack(pady=5)

root.bind('<Return>', generate_password)
root.mainloop()