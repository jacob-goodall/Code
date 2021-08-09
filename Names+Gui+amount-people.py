import turtle, time
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

filepath = ""
def open_file():
    global filepath, sorted_new_list, window
    x1 = entry1.get()
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("CSV", "*.csv*")]
    )
    if not filepath:
        return
    print(filepath)
    window.title(f"File Selector - {filepath}")

    with open(filepath) as a:
        lines = a.readlines()
    new_list = [s.replace("\n", "") for s in lines]
    print(new_list)
    sorted_new_list = sorted(new_list)
    print(sorted_new_list)
    
    file = open(filepath,"r")
    Counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    print(Counter)

    
    file.close()

    print("Number of People in List:",Counter)
    for elem in sorted_new_list:
          print(elem)

def tkamount():
    global root, x1
    x1 = 0
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 400, height = 300)
    canvas1.pack()

    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry1)

    def getamountpeople():  
        x1 = entry1.get()
        x1 = 'Selected Amount:', x1 
        button3.config(text=x1)
        # do something with the number

    def quiting():
        root.destroy()
        
    button1 = tk.Button(text='Amount of People wanted to plot', command=getamountpeople)
    button2 = tk.Button(text='Done (Once Selected Number)', command=quiting )
    button3 = tk.Label(text= x1)
    canvas1.create_window(200, 180, window=button1)
    canvas1.create_window(200,220, window=button2)
    canvas1.create_window(200, 50, window=button3)

    root.mainloop()
    tkfile()
        
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
    turtles()

def turtles():

  WIDTH, HEIGHT = 800, 800

  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title bar
  screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
  turtle.tracer(0)
  flag = turtle.Turtle()

  start = 100
  flag.penup()
  flag.goto(0,50)
  for i in range(3):
      for i in range (8):
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
  name.goto(0,50)

  l = [ValueError, TypeError]

  for  x in range(3):
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

tkamount()
