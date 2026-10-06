import tkinter as tk

def on_click(event):
    text=event.widget.cget("text")
    if text == "=":
        try:
            result=eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_var=tk.StringVar()
entry=tk.Entry(root, textvar=entry_var, font="Arial 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons= [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
]

frame=tk.Frame(root)
frame.pack()

for row in buttons:
    button_row=tk.Frame(frame)
    button_row.pack()
    for btn_text in row:
        btn=tk.Button(button_row,text=btn_text, font= "Arial 20 bold",height=2, width=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()