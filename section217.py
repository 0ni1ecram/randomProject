''' Compute BMI '''

# Prompt user input weight(pounds), height(inch)
pound = eval(input("Insert weight(ponds): "))
inch = eval(input("Insert height(inch): "))

# Weight and Height convversion to respective units
weight = pound * 0.45359237
height = inch * 0.0254

# Compute the BMI
bmi = weight / (height**2)

# Display the BMI
print("BMI is",bmi)
