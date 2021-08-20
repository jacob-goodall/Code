# IMPORTANT
# To get working install easygui through package manager or pip install easygui

# Importing Files
from easygui import *
import sys, turtle
from itertools import chain

# First Run Function
def first():
    # File Opening
    def opening():
        # Gets Filepath from user input
        filepath = fileopenbox(title="Select File", multiple=False, filetypes="*.txt")
        # Passes on to next function (Reading the File)
        reading(filepath)

    # Reading the File
    def reading(filepath):
        # Opens file as a
        with open(filepath) as a:
            lines = a.readlines()
            # reads individual lines
        # Disgarding \n
        new_list = [s.replace("\n", "") for s in lines]
        # sorts list by alpabet (Probably Not required as sorted in to wars later)
        sorted_new_list = sorted(new_list)
        # Splits terms up in to separate lists with First name, Second name and war.
        first1 = [i.split(" ")[0] for i in sorted_new_list]
        second2 = [i.split(" ")[1] for i in sorted_new_list]
        third3 = [i.split(" ")[2] for i in sorted_new_list]
        # Turns string to in individual lists and then to sublists of each person, with firstname secondname and war inside lists of each person,
        # Therefore it makes its easier to sort by war
        x4 = list(chain.from_iterable(zip(first1, second2, third3)))
        x5 = [x4[x : x + 3] for x in range(0, len(x4), 3)]

        # Sorts by war
        def Sort(x5):
            # gets third term which is war and sorts by alphabet
            x5.sort(key=lambda x: x[2])
            return x5

        Sort(x5)
        # Setting up Variables
        order = 0
        boer = 0
        ww1 = 0
        ww2 = 0
        # making lists
        listing = list(map(" ".join, x5))
        # maths of how many names for each war
        for x1 in listing:
            if "BOER" in x1:
                boer += 1
            if "WWI" and not "WWII" in x1:
                ww1 += 1
            if "WWII" in x1:
                ww2 += 1
        ww1 = ww2 - ww1
        # Splitting up lists in order of war
        war_boer = listing[:boer]
        war_1 = listing[boer : boer + ww1]
        war_2 = listing[boer + ww1 :]
        # Sorting each war in alpabetical order
        sorted_war_boer = sorted(war_boer)
        sorted_war_1 = sorted(war_1)
        sorted_war_2 = sorted(war_2)
        # recombining wars to be printed out by a turtle
        combinded_war = sorted_war_boer + sorted_war_1 + sorted_war_2

        file = open(filepath, "r")
        Counter = 0

        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")
        # Counting amount of lines
        for i in CoList:
            if i:
                Counter += 1

        file.close()
        second(combinded_war, Counter)

    opening()


# Second run main function
def second(combinded_war, Counter):
    # Setting up the gui
    msg = "Enter Info about task"
    title = "Cross Plotter"
    # labels for gui inputs
    naming = "Amount of people to plot Number must be under:", Counter
    # Inputing values
    fieldNames = ["Width Of Area (m)", "Length of Area (m)", naming]
    # Formatting gui
    fieldValues = multenterbox(msg, title, fieldNames)
    if fieldValues is None:
        sys.exit(0)
    # make sure that none of the fields were left blank
    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
                errmsg += "{} is a required field.\n\n".format(name)
        if errmsg == "":
            break  # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    # Moving to Turtles
    turtles(combinded_war, fieldValues[0], fieldValues[1], fieldValues[2], Counter)


def turtles(combinded_war, width, height, amount_of_people, Counter):
    # Converting values to INT's
    length = int(width)
    height = int(height)
    amount_of_people = int(amount_of_people)
    # If wanting to plot more people then amount of names in files
    if amount_of_people > Counter:
        print("error")
        # Resetting so the user can enter correct values
        second(combinded_war, Counter)
    # Amount of names that can fit on each axis
    x = int(length * 2)
    y = int(height * 2)
    # total amount of people able to fit
    total_amount_able_to_fit = length * height
    # Making an INT
    total_amount_able_to_fit = int(total_amount_able_to_fit)
    # Erroring if allocated space isn't enough space for amount of names wanted to plot
    if total_amount_able_to_fit <= amount_of_people:
        print("Error Too little space")
        # resetting
        second(combinded_war, Counter)
    # Screen Setup
    WIDTH, HEIGHT = 1400, 520
    screen = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    # Flag Turtle
    def flag(combinded_war, width, height, amount_of_people, Counter, x, y):
        # making the turtle speedy
        turtle.speed(0)
        # Defining Turtle
        flag = turtle.Turtle()
        # Start point
        start = 0
        # Pen Up
        flag.penup()
        flag.goto(0, 50)
        flag.backward(150)
        order1 = 0
        # Looping through and plotting dots accordingly
        for i in range(x):
            for i1 in range(y):
                flag.penup()
                flag.forward(150)
                flag.dot()
                flag.penup()
                order1 += 1
                # stopping when met people requirement
                if order1 >= amount_of_people:
                    name(combinded_war, width, height, amount_of_people, Counter, x, y)
            start += 150
            flag.goto(-150, start)

    # name writing turtle
    def name(combinded_war, width, height, amount_of_people, Counter, x, y):
        # making names appare instantly
        turtle.tracer(0)

        start1 = 0
        order = 0
        name = turtle.Turtle()
        name.penup()
        name.goto(0, 50)
        name.backward(150)
        # Looping through and plotting names accordingly

        for x2 in range(x):
            for x3 in range(y):
                name.penup()
                name.forward(150)
                name.write(combinded_war[order])
                order += 1
                # stopping and waiting till click once done
                if order >= amount_of_people:
                    turtle.exitonclick()

            start1 += 150
            print(start1)
            name.goto(-150, start1)

    # Starting the program
    flag(combinded_war, width, height, amount_of_people, Counter, x, y)


first()
