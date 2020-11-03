from gturtle import *

makeTurtle()
hideTurtle()

def square():
    repeat 4:
        forward(50)
        right(90)
        
def row():
    repeat 4:
        square()
        right(90)
        forward(50)
        left(90)
    left(90)
    forward(4*50)
    right(90)
    forward(50)

setPenWidth(2)
setPenColor("chocolate")

repeat 6:
    row()
