from gturtle import *

makeTurtle()

hideTurtle()

right(18)

laenge = 10

repeat 10:
    repeat 5:
        forward(laenge)
        right(180-36)
        forward(laenge)
        left(72)
    penUp()
    left(60)
    forward(10)
    right(60)
    penDown()
    laenge += 20
    
