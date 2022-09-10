''' Acceleration '''

# Prompt user to enter the starting velocity, ending velocity(m/s) and time span t(sec)
v0,v1,t = eval(input("Enter v0, v1 and t: "))

# Averqage acceleation computation
a = (v1 - v0) / t

# Display the result
print("The average acceleration is", a)