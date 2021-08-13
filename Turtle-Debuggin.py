import time, turtle


WIDTH, HEIGHT = 1400, 520
screen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

turtle.speed(0)
flag = turtle.Turtle()

start = 0
flag.penup()
flag.goto(0, 50)
flag.backward(150)
for i in range(4):
    for i in range(6):
            flag.penup()
            flag.forward(150)
            flag.dot()
            flag.penup()
    start += 150
    flag.goto(-150, start)
    
turtle.tracer(0)

start1 = 0
order = 0
name = turtle.Turtle()
name.penup()
name.goto(0, 50)
name.backward(150)

for x in range(4):
    for x in range(6):
        name.penup()
        name.forward(150)
        name.write("x")
        order += 1
        if order >= Counter:
            break
            time.sleep(100)
    start1 += 150
    print(start1)
    name.goto(-150, start1)
    

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