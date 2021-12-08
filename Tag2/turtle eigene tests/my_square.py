# For loop+function turtle
import turtle as t

def my_square():
    for x in range(4):
        t.forward(100)
        t.right(90)

    t.done()

my_square()