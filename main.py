# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
lines.speed(0)
wn = trtl.Screen()

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()


# Code for 80 point version goes here
def v80():
    startX = -490
    startY = -300
    endX = 490
    endY = -288.75

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX += 17.5
        endY += 11.25

        lines.pendown()





# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80()

    startX = 490
    startY = -300
    endX = -490
    endY = -288.75

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX -= 17.5
        endY += 11.25

        lines.pendown()




# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90()
    startX = -490
    startY = 330
    endX = 490
    endY = 318.75

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX += 17.5
        endY -= 11.25
        lines.pendown()

    startX = 490
    startY = 330
    endX = -490
    endY = 318.75

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX -= 17.5
        endY -= 11.25
        lines.pendown()




# Code for the 110 point version here
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()

    startX = -245
    startY = -145
    endX = 245
    endY = -144.375

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX += 8.75
        endY += 5.625
        lines.pendown()

    startX = 245
    startY = -145
    endX = -245
    endY = -144.375

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX -= 8.75
        endY += 5.625
        lines.pendown()

    startX = -245
    startY = 180
    endX = 245
    endY = 174.375

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX += 8.75
        endY -= 5.625
        lines.pendown()

    startX = 245
    startY = 180
    endX = -245
    endY = 174.375

    for line in range(56):
        lines.penup()
        lines.goto(startX, startY)
        lines.pendown()
        lines.goto(endX, endY)
        startX -= 8.75
        endY -= 5.625
        lines.pendown()

setupScreen()
setupBox()
v110()

wn = trtl.Screen()
wn.mainloop()