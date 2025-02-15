import turtle

x=turtle.Turtle()
x.shape("turtle")
x.color("red","yellow")
x.begin_fill()


for _ in range(4):
    x.forward(100)
    x.right(90)
x.end_fill()
turtle.done()