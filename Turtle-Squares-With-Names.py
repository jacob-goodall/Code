import turtle, time



import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

filepath = ""
def open_file():
    global filepath
    global sorted_new_list
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("CSV", "*.csv*")]
    )
    if not filepath:
        return
    print(filepath)
    window.title(f"File Selector - {filepath}")

    f = open(filepath,'r')
    message = f.read()
    print(message)
    with open(filepath) as a:
        lines = a.readlines()
    new_list = [s.replace("\n", "") for s in lines]
    print(new_list)
    sorted_new_list = sorted(new_list)
    print(sorted_new_list)
    
    f.close()
    file = open(filepath,"r")
    Counter = 0
    
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1

    print("Number of People in List:",Counter)
    for elem in sorted_new_list:
          print(elem)



window = tk.Tk()
window.title("File Selector")

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open Files", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
fr_buttons.grid(row=0, column=0, sticky="ns")

window.mainloop()



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
      if order >= 17:
        break
        time.sleep(100)

        
    name.goto(0, start1)
    start1 = start1 + 50     

turtle.done()
file.close()

