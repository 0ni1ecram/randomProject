''' Find Run-way length '''
# Given airplane acceleration and speed
v = eval(input("Insert the speed of the plane (m/s): "))    # Speed of the plane in meter per second
a = eval(input("Insert the acceleration of the plane (m/s2): "))    # acceleration of the plane in meter per second squared

# Computing Formula
length = v**2 / (2*a)

# Result
print("The minimum runwaylength of this airplane is",length,"meters")