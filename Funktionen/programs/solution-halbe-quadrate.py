from gturtle import *

makeTurtle()
hideTurtle()

def square(side):
    repeat 4:
        forward(side)
        right(90)
        
size = 256
repeat 8:
    square(size)
    right(90)
    forward(size)
    left(90)
    size /= 2
