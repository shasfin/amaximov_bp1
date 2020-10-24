from gturtle import *

makeTurtle()

    
hideTurtle()

setPenWidth(2)

penUp()
left(90)
forward(127)
right(180)
penDown()

red = 0
green = 0
blue = 255

# Hintergrund
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

# Gehe zur Mitte
penUp()
forward(127)
right(90)
forward(127)
left(180)
penDown()

# Schneeflocke
# setPenColor("white")
repeat 6:
    laenge = 10
    # Strahl
    repeat 5:
        forward(15)
        right(30)
        forward(laenge)
        back(laenge)
        left(60)
        forward(laenge)
        back(laenge)
        right(30)
        laenge += 10
    back(75)
    # Drehen
    right(60)


