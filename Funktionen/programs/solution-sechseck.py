from gturtle import *

makeTurtle()
hideTurtle()

def triangle():
    repeat 3:
        forward(100)
        right(120)

right(30)        
repeat 6:
    triangle()
    right(60)
