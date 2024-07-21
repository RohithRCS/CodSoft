import tkinter as tk
from tkinter import messagebox,simpledialog

def add(event=None):
    task=entry.get().strip()
    if task:
        task=task.capitalize()
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Please Enter a Task")

def delete(event=None):
    selected_task=listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning","Please Select a Task to Delete")

def update():
    try:
        selected_task=listbox.curselection()[0]
        old_task=listbox.get(selected_task)
        new_task=simpledialog.askstring("Update Task","Update Task",initialvalue=old_task)
        if new_task:
            listbox.delete(selected_task)
            listbox.insert(selected_task,new_task.capitalize())
    except IndexError:
        messagebox.showwarning("Warning", "Please Select a Task to Update")

root=tk.Tk()
root.title("TO-Do List")
root.geometry("400x380")

entry=tk.Entry(root,width=60)
entry.pack(pady=15)
entry.bind("<Return>",add)

listbox=tk.Listbox(root,width=60,height=15)
listbox.pack(pady=15)
listbox.bind("<Delete>",delete)

frame=tk.Frame(root)
frame.pack(pady=15)

add_button=tk.Button(frame,text="Add Task",command=add)
add_button.pack(side=tk.LEFT,padx=15)

delete_button=tk.Button(frame,text="Delete Task",command=delete)
delete_button.pack(side=tk.LEFT,padx=15)

update_button=tk.Button(frame,text="Update Task",command=update)
update_button.pack(side=tk.LEFT,padx=15)

root.mainloop()
