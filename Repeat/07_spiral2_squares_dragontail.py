from gturtle import *

makeTurtle()

hideTurtle()

laenge = 1
winkel = 15


repeat 120:
    repeat 4:
        forward(laenge*3)
        right(90)
    forward(laenge)
    right(winkel)
    laenge += 0.2
    winkel -= 0.1

