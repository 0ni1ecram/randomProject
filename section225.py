''' Drawing a Rectangle '''
import turtle

# Prompt uswr to enter center, length and width of rectangle
x,y = eval(input("Insert center of the rectangle: "))
length = eval(input("Insert the length of the rectangle: "))
width = eval(input("Insert the width of the rectangle: "))

# Drawing the rectangle
turtle.penup()
turtle.goto(x,y)
turtle.forward(length/2)
turtle.pendown()
turtle.left(90)
turtle.forward(width/2)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(width/2)