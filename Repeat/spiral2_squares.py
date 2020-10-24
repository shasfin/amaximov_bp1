from gturtle import *

makeTurtle()

hideTurtle()

laenge = 5
winkel = 15


repeat 60:
    repeat 4:
        forward(laenge)
        right(90)
    right(winkel)
    laenge += 3
    winkel -= 0.1

