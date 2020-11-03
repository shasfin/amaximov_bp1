from gturtle import *

makeTurtle()
hideTurtle()

def polygon(n):
    repeat n:
        forward(100)
        right(360/n)

left(90)       
setPenWidth(3)
setPenColor("purple")

nofSides = 3
repeat 5:
    polygon(nofSides)
    nofSides += 1
