''' Compute Distance '''

# Enter first pont with two point floats
x1, y1 = eval(input("Enter x1 and y2 for point 1: "))

# Enter second point with two floats
x2, y2 = eval(input("Enter x2 and y2 for point2: "))

# Compute distance
distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

print('Distance between points is: ', distance)
