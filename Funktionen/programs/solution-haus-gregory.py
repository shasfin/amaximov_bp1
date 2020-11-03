from gturtle import *

makeTurtle()
hideTurtle()

def square():
    repeat 4:
        forward(100)
        right(90)
        
def square15():
    repeat 4:
        forward(15)
        right(90)
        
def triangle():
    repeat 3:
        forward(100)
        right(120)

def window():
    repeat 4:
        square15()
        penUp()
        forward(30)
        penDown()
        right(90)
    
def door():
    repeat 2:
        forward(50)
        right(90)
        forward(30)
        right(90)

def drawDoor():
    penUp()
    right(90)
    forward(35)
    left(90)
    penDown()
    
    door()
    
    penUp()
    left(90)
    forward(35)
    right(90)
    penDown()
        
def drawWindows():
    repeat 2:
        penUp()
        right(90)
        forward(10)
        left(90)
        penDown()
        
        window()
        
        penUp()
        right(90)
        forward(40)
        left(90)
        penDown()
    penUp()
    left(90)
    forward(100)
    right(90)
    penDown()
    
def drawRoof():
    right(30)
    triangle()
    left(30)
        
    
setPenColor("dark green")
square()

setPenColor("brown")
drawDoor()

setPenColor("light blue")
penUp()
forward(60)
penDown()
drawWindows()

setPenColor("red")
penUp()
forward(40)
penDown()
drawRoof()


