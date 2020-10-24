from gturtle import *

makeTurtle()
hideTurtle()

penUp()
left(90)
forward(300)
right(180)
penDown()

setPenWidth(20)

red = 255
green = 255
blue = 0

repeat 255:
    setPenColor(red, green, blue)
    forward(2)
    green -= 1
