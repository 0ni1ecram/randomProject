''' Area of a Triangle '''

# Prompt user to enter three points
x1,y1 = eval(input("Enter points of the triangle(x1,y1): "))
x2,y2 = eval(input("Enter points of the triangle(x2,y2): "))
x3,y3 = eval(input("Enter points of the triangle(x3,y3): "))

# Computing area of a triangle
side1 = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
side2 = ((x2-x3)**2 + (y2-y3)**2) ** 0.5
side3 = ((x3-x1)**2 + (y3-y1)**2) ** 0.5

s = (side1 + side2 + side3) / 2
area = (s * (s-side1) * (s-side2) * (s-side3)) ** 0.5

# Displays the area of the triangle
print("\nThe area of the triangle is", area)