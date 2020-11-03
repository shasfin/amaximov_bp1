from gturtle import *

makeTurtle()
hideTurtle()

def square(side):
    repeat 4:
        forward(side)
        right(90)

size = 250
decrement = 30
repeat 8:
    square(size)
    size -= decrement
    
    penUp()
    forward(decrement/2)
    right(90)
    forward(decrement/2)
    left(90)
    penDown()
    
