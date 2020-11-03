from gturtle import *

makeTurtle()
hideTurtle()

def triangle(side):
    repeat 3:
        forward(side)
        right(120)

right(30)        
size = 256
repeat 8:
    triangle(size)
    size /= 2
    forward(size)
    left(60)

