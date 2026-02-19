import tkinter as tk

def click(x):
    Entry.insert(tk.END, x)

def clear():
    Entry.delete(0, tk.END)

def calc():
    try:
        result = eval(Entry.get())
        Entry.delete(0, tk.END)
        Entry.insert(0, result)
    except:
        Entry.delete(0, tk.END)
        Entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="beige")
root.resizable(True, True)

Entry = tk.Entry(root, font=("Lucida Console", 20),
                 bg="#2d2d2d", fg="white",
                 bd=0, justify="right")
Entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r = 1
c = 0

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: click(x)
    tk.Button(root, text=b, command=cmd,
              font=("Gill Sans MT", 14),
              width=5, height=2,
              bg="orange" if b in "+-/*=" else "gray",
              fg="white", bd=0).grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c == 4:
        r += 1
        c = 0

tk.Button(root, text="C", font=("Segoe UI", 14),
          command=clear, bg="red",
          fg="white", bd=0).grid(row=r, column=0, columnspan=4, sticky="we")

root.mainloop()
