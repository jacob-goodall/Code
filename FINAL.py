from easygui import *
import sys, turtle, time

def first():
  def opening():
    filepath  = fileopenbox(title="Select File", multiple=False, filetypes="*.txt")
    print(filepath)
    reading(filepath)

  def reading(filepath):
    f = open(filepath,'r')
    message = f.read()
    with open(filepath) as a:
        lines = a.readlines()
    new_list = [s.replace("\n", "") for s in lines]
    sorted_new_list = sorted(new_list)
    
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
    print(sorted_new_list)
    second(sorted_new_list)

def second(sorted_new_list):
  msg = "Enter Info about task"
  title = "Cross Plotter"
  fieldNames = ["Width Of Area", "Length of Area", "Amount of people to plot"]
  fieldValues = multenterbox(msg, title, fieldNames)
  if fieldValues is None:
      #need to make it restart
      sys.exit(0)
  # make sure that none of the fields were left blank
  while 1:
      errmsg = ""
      for i, name in enumerate(fieldNames):
          if fieldValues[i].strip() == "":
            errmsg += "{} is a required field.\n\n".format(name)
      if errmsg == "":
          break # no problems found
      fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
      if fieldValues is None:
          break
  print(fieldValues)
  turtles()

def turtles():
  global x1

  WIDTH, HEIGHT = 800, 800
  screen = turtle.Turtle()
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
  #turtle.tracer(0)
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
  global sorted_new_list
  name = turtle.Turtle()
  name.penup()
  name.goto(0, 50)

  for x in range(3):
      for x in range(8):
          name.penup()
          name.forward(150)
          print(x)
          x =+ 1 
          print(sorted_new_list)
          name.write(sorted_new_list)
          order += 1
          print("Order:", order)
          if order >= 17:
              break
              time.sleep(100)

      name.goto(0, start1)
      start1 = start1 + 50

  turtle.done()







first()