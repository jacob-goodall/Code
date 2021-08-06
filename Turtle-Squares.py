import turtle

WIDTH, HEIGHT = 450, 450

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

flag = turtle.Turtle()

start = 100
flag.penup()
flag.goto(0,50)
for i in range(3):
    for i in range (8):
        flag.penup()
        flag.forward(60)
        flag.dot()
        flag.penup()

    flag.goto(0, start)
    start = start + 50

start1 = 100
name = turtle.Turtle()
name.penup()
name.goto(0,50)
for  x in range(3):
    for x in range(8):
        name.penup()
        name.forward(60)
        name.write("Test")
        
    name.goto(0, start1)
    start1 = start1 + 50
        

turtle.done()


