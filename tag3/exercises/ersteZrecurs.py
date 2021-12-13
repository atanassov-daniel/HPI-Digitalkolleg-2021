import math
import turtle
s = turtle.getscreen()
t = turtle.Turtle()

def quadrat(size):
    if size - 10 <= 0:
        s.exitonclick()
        return

    for x in range(4):
        t.forward(size)
        t.right(90)

    t.penup()
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(-90)
    t.pendown()
    quadrat(size - 10)
    # quadrat(size - math.sqrt(2* 10**2)) - per presentation

quadrat(100)
