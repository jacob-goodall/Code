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

#flag.goto(0,50)

turtle.done()

