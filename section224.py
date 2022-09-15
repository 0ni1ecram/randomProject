# Drawing 4 Hexagons
import turtle

turtle.penup()
turtle.goto(0,0)
turtle.penup()

# Hexagon 1
turtle.goto(1,15)
turtle.pendown()
turtle.goto(1, 15)
turtle.goto(15, 1)
turtle.goto(45, 1)
turtle.goto(60,15)
turtle.goto(60,45)
turtle.goto(45,60)
turtle.goto(15,60)
turtle.goto(1,45)
turtle.goto(1,15)
turtle.penup()

# Hexagon 2
turtle.goto(1,-15)
turtle.pendown()
turtle.goto(15, -1)
turtle.goto(45, -1)
turtle.goto(60, -15)
turtle.goto(60, -45)
turtle.goto(45, -60)
turtle.goto(15, -60)
turtle.goto(1, -45)
turtle.goto(1, -15)
turtle.penup()

# Hexagon 3
turtle.goto(-15, 1)
turtle.pendown()
turtle.goto(-45, 1)
turtle.goto(-60,15)
turtle.goto(-60,45)
turtle.goto(-45,60)
turtle.goto(-15,60)
turtle.goto(-1,45)
turtle.goto(-1,15)
turtle.goto(-15, 1)
turtle.penup()

# Hexagon 4
turtle.goto(-15, -1)
turtle.pendown()
turtle.goto(-45, -1)
turtle.goto(-60, -15)
turtle.goto(-60, -45)
turtle.goto(-45, -60)
turtle.goto(-15, -60)
turtle.goto(-1, -45)
turtle.goto(-1, -15)
turtle.goto(-15, -1)
turtle.penup()
