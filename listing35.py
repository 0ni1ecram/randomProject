# Today we are gonna learn how to draw a triangle in python using turtle

# Step 1
import turtle

# Step 2
''' Set the thickness of the line '''
turtle.pensize(3) # Sets the pen / thickness of the line to 3 pixels

# Step 3
''' Pull the pen up so that a mess is not made '''
turtle.penup()

# Step 4
''' Set a coordinate on the page where you want to draw your triangle '''
turtle.goto(-250, -50)

# Step 5
''' Put the pen down to start drawing '''
turtle.pendown()

# Step 6
''' Draw the Triangle '''
turtle.circle(40, steps=3) # Where the 40- represents the radius of the triangle &
                            # The "step = 3" represents the 3 points of the triangle

# Step 7
''' Freeze the window to see the result '''
# turtle.done()

''' Drawing a Square '''
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=4)

''' Drawing a Pentaon '''
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps=5)

''' Drawing a Hexagon '''
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps=6)

''' Drawing a Circle '''
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)

turtle.done()