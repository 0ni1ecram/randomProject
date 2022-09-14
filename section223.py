# Drawing 4 circles at the center of a page
import turtle

# Prompt user to enter the radius(r)
r = eval(input("Insert radius of circle: "))

# Draw 4 circles at the center of the screen
turtle.goto(0,0)
turtle.penup()
# Circle 1
turtle.goto(r , r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
# Circle 2
turtle.goto(r , -r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
# Circle 3
turtle.goto(-r , r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
#Circle 4
turtle.goto(-r , -r)
turtle.pendown()
turtle.circle(r)
turtle.penup()