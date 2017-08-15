"""
An introduction to variables and functions for EYW II using the Turtle library. 
"""

# import the turtle library so that we may use all of its functions
import turtle

# create a screen to display our graphics
# any functions called from the turtle library must be preceded by 'turtle.'
window = turtle.Screen()

# create a turtle named shelly (hehehe. get it?? cuz turtles have a shell)
shelly = turtle.Turtle()

# move the shelly turtle forward a distance of 50 pixels and rotate 90 degrees to the left
shelly.forward(50)
shelly.left(90)
shelly.forward(50)
shelly.left(90)
shelly.forward(50)
shelly.left(90)
shelly.forward(50)
shelly.left(90)

# keep the window open and running, even though the program has ended
# keep this statement at the end of your program
turtle.mainloop()
