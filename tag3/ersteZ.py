import turtle

def zeichne(n):
    s = turtle.getscreen()
    t = turtle.Turtle()

    for x in range(4):
        t.forward(n)
        t.right(90)

    s.exitonclick()

zeichne(100)