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
    second(sorted_new_list, Counter)
  opening()

def second(sorted_new_list, Counter):
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
  turtles(sorted_new_list, fieldValues[0], fieldValues[1], fieldValues[2], Counter)

def turtles(sorted_new_list, width, height, amount_of_people, Counter):
  width = int(width)
  height = int(height)
  WIDTH, HEIGHT = 1400, 520
  screen = turtle.Turtle()
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
  #turtle.tracer(0)
  flag = turtle.Turtle()

  start = 100
  flag.penup()
  flag.goto(0, 50)
  flag.backward(150)
  for i in range(3):
      for i in range(8):
          flag.penup()
          flag.forward(150)
          flag.dot()
          flag.penup()

      flag.goto(-150, start)
      start = start + 50

  start1 = 100
  order = 0
  name = turtle.Turtle()
  name.penup()
  name.goto(0, 50)
  name.backward(150)

  for x in range(3):
      for x in range(8):
          name.penup()
          name.forward(150)
          name.write(sorted_new_list[order])
          order += 1
          if order >= Counter:
              break
              time.sleep(100)

      name.goto(-150, start1)
      start1 = start1 + 50

  measure = turtle.Turtle()
  measure.penup()
  

  turtle.done()







first()