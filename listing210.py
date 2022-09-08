''' Compute Distance Graphics '''

import turtle

# Prompt inputing two points
x1, y1 = eval(input("Insert co-ordinatesA (x,y): "))
x2, y2 = eval(input("insert co-ordinatesB (x,y):"))

# Compute distance
distance = ((x1 - x2)** 2 + (y1 - y2)** 2)** 0.5
print(distance)
# Display two points connecting the line
turtle.penup()
turtle.goto(x1,y1) # Co-ordinateA
turtle.pendown()
turtle.write("PointA")
turtle.goto(x2,y2) # Co-ordinateB
turtle.write("PointB")
turtle.penup()

# Move to center of the line
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.pendown()
turtle.write(distance)

turtle.penup()