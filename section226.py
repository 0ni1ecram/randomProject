''' Draw a Circle '''
import turtle

# Prompt user to enter center and radius
radius = eval(input("Insert the radius of the circle: "))
x,y = eval(input("Insert the center of the circle: "))

# Compute the area of the circle
area = 3.14 * radius**2

# Display the area
turtle.penup()
turtle.goto(x,y)
turtle.write(area)
turtle.goto(x,y)
turtle.right(90)
turtle.pendown()
turtle.circle(radius)
