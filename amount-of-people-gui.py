import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getamountpeople():  
    x1 = entry1.get()
    # do something with the number
    
    
button1 = tk.Button(text='Amount of People wanted to plot', command=getamountpeople)
canvas1.create_window(200, 180, window=button1)

root.mainloop()