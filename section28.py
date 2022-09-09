''' Calulate Energy '''
# Prompt user to enter water in kilograms
M = eval(input("Insert mass of water in kilograms: "))

# Prompt user to Enter tepmratures of water
initialTemp = eval(input("Insert initial water temprature: "))
finalTemp = eval(input("Insert final water temprature: "))

# Computation
Q = M * (finalTemp - initialTemp) * 4184

# Energy required to heat water from initial temp to Final temp
print(f'The energy needed is {Q}')
