import turtle, time
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

global sorted_new_list
sorted_new_list = []
errors = [ValueError, TypeError]

filepath = ""


def open_file():
    global filepath, sorted_new_list, window
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("CSV", "*.csv*")])
    if not filepath:
        return

    window.title(f"File Selector - {filepath}")

    with open(filepath) as a:
        lines = a.readlines()
    new_list = [s.replace("\n", "") for s in lines]
    sorted_new_list = sorted(new_list)

    file = open(filepath, "r")
    Counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    print(Counter)
    print(filepath)

    file.close()

    print("Number of People in List:", Counter)


def tkamount():
    global root, x1
    x1 = 0
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=400, height=300)
    canvas1.pack()

    entry1 = tk.Entry(root)

    canvas1.create_window(200, 140, window=entry1)

    def getamountpeople():
        x1 = entry1.get()
        x1 = "Selected Amount:", x1
        button3.config(text=x1)
        # do something with the number

    def quiting():
        root.destroy()

    button1 = tk.Button(text="Amount of People wanted to plot", command=getamountpeople)
    button2 = tk.Button(text="Done (Once Selected Number)", command=quiting)
    button3 = tk.Label(text=x1)
    canvas1.create_window(200, 180, window=button1)
    canvas1.create_window(200, 220, window=button2)
    canvas1.create_window(200, 50, window=button3)

    root.mainloop()
    turtles()


def tkfile():
    global window
    window = tk.Tk()
    window.title("File Selector")
    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open Files", command=open_file)
    btn_open.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
    fr_buttons.grid(row=0, column=0, sticky="ns")
    window.mainloop()
    tkamount()


def turtles():
    global x1

    WIDTH, HEIGHT = 800, 800

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title bar
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    turtle.tracer(0)
    flag = turtle.Turtle()

    start = 100
    flag.penup()
    flag.goto(0, 50)
    for i in range(3):
        for i in range(8):
            flag.penup()
            flag.forward(150)
            flag.dot()
            flag.penup()

        flag.goto(0, start)
        start = start + 50

    start1 = 100
    order = 0
    name = turtle.Turtle()
    name.penup()
    name.goto(0, 50)

    for x in range(3):
        for x in range(8):
            name.penup()
            name.forward(150)
            name.write(sorted_new_list[order])
            order += 1
            if order >= x1:
                break
                time.sleep(100)

        name.goto(0, start1)
        start1 = start1 + 50

    turtle.done()

def sizeofarea():
    def show_entry_fields():
        global x, y
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
    tkfile()

sizeofarea()
