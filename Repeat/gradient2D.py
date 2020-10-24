from gturtle import *

makeTurtle()

    
hideTurtle()

setPenWidth(2)

penUp()
left(90)
forward(500)
right(180)
penDown()

red = 0
green = 0
blue = 255

repeat 255:
    red = 0
    repeat 255:
        setPenColor(red, green, blue)
        forward(1)
        red += 1
    green += 1
    penUp()
    back(255)
    penDown()
    left(90)
    forward(1)
    right(90)

