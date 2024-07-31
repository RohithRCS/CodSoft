import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []
        self.current_view_contacts = []

        self.form_frame = tk.Frame(root, padx=10, pady=10)
        self.form_frame.pack(pady=10)

        self.labels = ["Name", "Phone Number", "Email", "Address"]
        self.entries = {}
        
        for i, label in enumerate(self.labels):
            tk.Label(self.form_frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            self.entries[label] = tk.Entry(self.form_frame, width=30)
            self.entries[label].grid(row=i, column=1, padx=10, pady=5)

        self.button_frame = tk.Frame(root, padx=10, pady=10)
        self.button_frame.pack(pady=10)

        button_colors = {
            "Add Contact": "lightgreen",
            "Update Contact": "lightblue",
            "Search Contact": "grey",
            "Delete Contact": "lightcoral"
        }

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, bg=button_colors["Add Contact"])
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, bg=button_colors["Update Contact"])
        self.update_button.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, bg=button_colors["Search Contact"])
        self.search_button.grid(row=0, column=2, padx=10, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, bg=button_colors["Delete Contact"])
        self.delete_button.grid(row=0, column=3, padx=10, pady=5)

        self.listbox_frame = tk.Frame(root, padx=10, pady=10)
        self.listbox_frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.listbox_frame, width=80, height=10)
        self.contact_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

        self.contact_listbox.bind("<<ListboxSelect>>", self.load_contact_details)
        
        self.root.bind("<Return>", lambda event: self.add_contact())
        self.root.bind("<Delete>", lambda event: self.delete_contact())

    def capitalize_fields(self, contact):
        contact['Name'] = contact['Name'].title()
        contact['Address'] = contact['Address'].title()
        return contact

    def add_contact(self):
        contact = {label: self.entries[label].get() for label in self.labels}
        contact = self.capitalize_fields(contact)
        if all(contact.values()):
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
            self.update_contact_list()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        self.current_view_contacts = self.contacts.copy()
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone Number']}")

    def search_contact(self):
        search_term = self.entries["Name"].get().strip() or self.entries["Phone Number"].get().strip()
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter a search term.")
            return

        search_term = search_term.lower()

        self.contact_listbox.delete(0, tk.END)
        self.current_view_contacts = [contact for contact in self.contacts if
                                      search_term in contact['Name'].lower() or
                                      search_term in contact['Phone Number'].lower()]

        if not self.current_view_contacts:
            messagebox.showinfo("Search Result", "No contacts found.")
        for contact in self.current_view_contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone Number']}")

    def load_contact_details(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index < len(self.current_view_contacts):
                contact = self.current_view_contacts[index]
                for label in self.labels:
                    self.entries[label].delete(0, tk.END)
                    self.entries[label].insert(0, contact[label])

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index < len(self.current_view_contacts):
                contact = self.current_view_contacts[index]
                contact_index = self.contacts.index(contact)

                updated_contact = {label: self.entries[label].get() for label in self.labels}
                updated_contact = self.capitalize_fields(updated_contact)
                if all(updated_contact.values()):
                    self.contacts[contact_index] = updated_contact
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    self.clear_entries()
                    self.update_contact_list()
                else:
                    messagebox.showwarning("Input Error", "All fields are required!")
            else:
                messagebox.showwarning("Selection Error", "Invalid selection.")
        else:
            messagebox.showwarning("Selection Error", "Select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index < len(self.current_view_contacts):
                contact = self.current_view_contacts[index]
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                self.update_contact_list()
            else:
                messagebox.showwarning("Selection Error", "Invalid selection.")
        else:
            messagebox.showwarning("Selection Error", "Select a contact to delete.")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()