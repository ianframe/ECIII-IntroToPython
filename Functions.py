"""
An introduction to functions for EYW II using the Turtle library. 
"""

# import the turtle library so that we may use all of its functions
import turtle

# create a variable named side_length whose value is 200
side_length = 50
# create a variable named angle whose value is 90. 
angle = 90

# create a screen to display our graphics
# any functions called from the turtle library must be preceded by 'turtle.'
window = turtle.Screen()
# establish the world's coordinate system
window.setworldcoordinates(-100, -100, 100, 100)

# create some turtles, change their shape to be a turtle shape
shelly = turtle.Turtle(shape='turtle')
wilford = turtle.Turtle(shape='turtle')
gilbert = turtle.Turtle(shape='turtle')
marge = turtle.Turtle(shape='turtle')

# lift the pen up and send each turtle to their designated starting location
shelly.penup()
shelly.goto(-75, -75)
wilford.penup()
wilford.goto(25, -75)
gilbert.penup()
gilbert.goto(25, 25)
marge.penup()
marge.goto(-75, 25)

# place the pen down for each turtle, and assign them a unique color
shelly.pen(pencolor='red', pendown=True, pensize=3)
wilford.pen(pencolor='green', pendown=True, pensize=3)
gilbert.pen(pencolor='blue', pendown=True, pensize=3)
marge.pen(pencolor='orange', pendown=True, pensize=3)

# keep the window open and running, even though the program has ended
# keep this statement at the end of your program
turtle.mainloop()
