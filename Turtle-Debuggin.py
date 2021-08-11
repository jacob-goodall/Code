import turtle
with open(Level3crosses.txt) as a:
        lines = a.readlines()
new_list = [s.replace("\n", "") for s in lines]
sorted_new_list = sorted(new_list)

WIDTH, HEIGHT = 800, 800
screen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
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
order = 17
name = turtle.Turtle()
name.penup()
name.goto(0, 50)

for x in range(3):
    for x in range(8):
        name.penup()
        name.right(90)
        name.forward(150)
        name.write(sorted_new_list[order])
        order += 1
        print(order)
        if order >= 17:
            break
            time.sleep(100)

    name.goto(0, start1)
    start1 = start1 + 50

turtle.done()