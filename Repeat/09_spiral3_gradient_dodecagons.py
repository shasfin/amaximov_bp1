from gturtle import *

makeTurtle()

hideTurtle()

laenge = 1
winkel = 15
red = 0
green = 200
blue = 0


repeat 120:
    setPenColor(red, green, blue)
    blue += 2
    repeat 12:
        forward(laenge*3)
        right(360/12)
    forward(laenge)
    right(winkel)
    laenge += 0.2
    winkel -= 0.1

