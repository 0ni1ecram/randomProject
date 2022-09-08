''' Compute Volume of a Cylinder '''
'''
#Requirements
Read radius & length
compute volume & area
'''
import math
PI = math.pi

# User input Radius & Length
radius = eval(input("Insert Radius of Cylinder: "))
length = eval(input("insert Lenght of Cylinder: "))

# Formula for Area
area = radius** 2 * PI
# Formula for volume
volume = area * length

print(f'The area is {area}\n The volume is {volume}')