''' Wind-Chill Temprature '''

# How cold is it outside
# Factors: temprature and wind speed,( relative humidity, sunshine)
ta = eval(input("Insert the temprature in Farnheit between (41 and -58): "))   # Temp outside in degrees Farenheit
v =  eval(input("Insert wind speed greater or equal to 2mph: "))               # Speed measured in mile per hour

# Computation not applicable for if: v< 2mph or for: 41 >t> -58
twc = 35.74 + 0.6215*(ta) - 35.75*(v**0.16) + 0.4275*(ta * v**0.16)

# Result
print("The wind chill index is:",twc)