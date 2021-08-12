from easygui import *
import sys, turtle, time
from itertools import chain



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
    first1 = [i.split(" ")[0] for i in sorted_new_list]
    second2 = [i.split(" ")[1] for i in sorted_new_list]
    third3 = [i.split(" ")[2] for i in sorted_new_list]


    test = list(chain.from_iterable(zip(first1, second2, third3)))
    chunks = [test[x : x + 3] for x in range(0, len(test), 3)]


    def Sort(chunks):

        chunks.sort(key=lambda x: x[2])
        return chunks


    Sort(chunks)
    order = 0
    boer = 0
    ww1 = 0
    ww2 = 0

    listing = list(map(" ".join, chunks))


    for x1 in listing:
        if "BOER" in x1:
            boer += 1
        if "WWI" and not "WWII" in x1:
            ww1 += 1
        if "WWII" in x1:
            ww2 += 1
    ww1 = ww2 - ww1
    war_boer = listing[:boer]
    war_1 = listing[boer : boer + ww1]
    war_2 = listing[boer + ww1 :]


    sorted_war_boer = sorted(war_boer)
    sorted_war_1 = sorted(war_1)
    sorted_war_2 = sorted(war_2)
    
    combinded_war = sorted_war_boer + sorted_war_1 + sorted_war_2
    

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
    
    second(combinded_war, Counter)
  opening()

def second(combinded_war, Counter):
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
  turtles(combinded_war, fieldValues[0], fieldValues[1], fieldValues[2], Counter)

def turtles(combinded_war, width, height, amount_of_people, Counter):
  width = int(width)
  height = int(height)
  WIDTH, HEIGHT = 1400, 520
  screen = turtle.Turtle()
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
  #turtle.tracer(0)
  turtle.speed(0)
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
          name.write(combinded_war[order])
          order += 1
          if order >= Counter:
              break
              time.sleep(100)

      name.goto(-150, start1)
      start1 = start1 + 50

  box = turtle.Turtle()
  box.penup()
  box.goto(0,0)
  box.pendown()
  box.forward(150 * 8)
  box.left(90)
  box.forward(175)
  box.left(90)
  box.forward(150 * 8)

  measure = turtle.Turtle()
  measure.penup()
  

  turtle.done()


first()