from gturtle import *

makeTurtle()

hideTurtle()

right(18)

clear("black")
setPenWidth(3)

red = 255
green = 0
blue = 0
laenge = 10

repeat 10:
    setPenColor(red, green, blue)
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
    green += 25
    laenge += 20
    
