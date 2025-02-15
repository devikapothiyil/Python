import turtle
t=turtle.Turtle()
t.speed(3)
turtle.colormode(255)
#Square
t.penup()
t.goto(-100,-100)
t.pendown()
t.fillcolor(150,75,0)
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-100,100)
t.pendown()
t.fillcolor(200,0,0)
t.begin_fill()
for _ in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()
t.penup()
t.goto(-30,-100)
t.pendown()
t.fillcolor(100,50,0)
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(120)
    t.left(90)
t.end_fill()



turtle.done()