import tkinter as tk

def show_entry_fields():
    x = e1.get()
    y = e2.get()

master = tk.Tk()
tk.Label(master, text="Width").grid(row=0)
tk.Label(master, text="Height").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()

