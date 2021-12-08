# Creating more complex squares
import turtle as t

def my_square():
    for x in range(4):
        t.forward(100)
        t.right(90)

my_square()

t.penup()
t.setpos(-100,100)
t.pencolor("lightblue")
t.pendown()
my_square()

t.done()