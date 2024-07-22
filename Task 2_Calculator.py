import tkinter as tk

def click(event):
    text=event.widget.cget("text")
    if text=="=":
        try:
            result.set(str(eval(entry.get())))
        except Exception as e:
            result.set("Error")
        entry.update()
    elif text=="C":
        result.set("")
        entry.update()
    else:
        result.set(entry.get()+text)
        entry.update()

root=tk.Tk()
root.geometry("380x450")
root.title("Simple Calculator")

result=tk.StringVar()
result.set("")

entry = tk.Entry(root,textvar=result,font="lucida 20 bold")
entry.pack(fill=tk.BOTH,ipadx=8,pady=10,padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/']

row,col=0,0
for button in buttons:
    color="light blue" if button.isdigit() else "light green"
    if button in ["C","="]:
        color="grey"
    b=tk.Button(frame,text=button,font="lucida 15 bold",relief=tk.RAISED,padx=20,pady=20,bg=color)
    b.grid(row=row,column=col,padx=5,pady=5)
    b.bind("<Button-1>",click)
    col += 1
    if col==4:
        col=0
        row += 1

root.mainloop()