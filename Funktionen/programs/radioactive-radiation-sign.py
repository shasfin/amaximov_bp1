from gturtle import *

def triangle(side):
    repeat 3:
        forward(side)
        right(120)

makeTurtle()

side = 50
repeat 3:
    triangle(side)
    side*=2
    right(120)
    
hideTurtle()
    