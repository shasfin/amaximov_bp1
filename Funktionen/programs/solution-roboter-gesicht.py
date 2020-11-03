from gturtle import *

makeTurtle()
hideTurtle()

def square(side):
    repeat 4:
        forward(side)
        right(90)

def eye():
    square(30)
    square(10)
    
def mouth():
    repeat 4:
        square(20)
        penUp()
        right(90)
        forward(30)
        left(90)
        penDown()
    penUp()
    left(90)
    forward(4*30)
    right(90)
    penDown()
    
def nose():
    square(30)
    
def drawEyes():
    repeat 2:
        penUp()
        right(90)
        forward(30)
        left(90)
        penDown()
        
        eye()
        
        penUp()
        right(90)
        forward(30)
        left(90)
        penDown()
    penUp()
    left(90)
    forward(4*30)
    right(90)
    penDown()
    
def drawMouth():
    penUp()
    right(90)
    forward(20)
    left(90)
    penDown()
    
    mouth()
    
    penUp()
    left(90)
    forward(20)
    right(90)
    penDown()
    
def drawNose():
    penUp()
    right(90)
    forward(60)
    left(90)
    penDown()
    
    nose()
    
    penUp()
    left(90)
    forward(60)
    right(90)
    penDown()
    
setPenColor("royal blue")
square(150)

setPenColor("lime green")
penUp()
forward(10)
penDown()
drawMouth()

setPenColor("red")
penUp()
forward(40)
penDown()
drawNose()

setPenColor("orange")
penUp()
forward(60)
penDown()
drawEyes()

