''' Formating Numbers and Strings '''
# One could use format function to return formatted strings

amount = 12618.98
interestRate = 0.0013
interest = amount * interestRate

# round(variable, 2)
print("Interest is:", round(interest, 2))

# format(variable, ".2f")
print("Interest is", format(interest, ".2f"))

print(format(57.467657, "10.2f"))
print(format(12345678.923, "10.2f"))
print(format(57.4, "10.2f"))

print(format(57.467657, "10.2e"))
print(format(0.0033923, "10.2e"))
print(format(57.4, "10.2e"))
print(format(57, "10.2e"))

print("\n") # Formating as percentage
print(format(0.54457, "10.2%"))
print(format(0.0033923, "10.2%"))
print(format(7.4, "10.2%"))
print(format(57, "10.2%"))

# Justifying format
print(format(57.467657, "10.2f"))
print(format(57.467657, "<10.2f"))

# Formating integers
print(format(59832, "10d"))
print(format(59832, "10x"))
print(format(59832, "10o"))
print(format(59832, "10b"))

# Formating Strings
print(format("Welcome to Python", "20s"))
print(format("Welcome to Python", "<20s"))
print(format("Welcome to Python", ">20s"))
print(format("Welcome to Python and Java", ">20s"))

# Return value from invoking the format function is a respective data type presented in a respective format
# Item extends

# Printout Statements
print("\n")
print(format(57.467567, "9.3f"))
print(format(12345678.923, "9.1f"))
print(format(57.4, ".2f"))
print(format(57.4, "10.2f"))

print(format(57.467567, "9.3e"))
print(format(12345678.923, "9.1e"))
print(format(57.4, ".2e"))
print(format(57.4, "10.2e"))

print(format(5789.467657, "9.3f"))
print(format(5789.467657, "<9.3f"))
print(format(5789.4, ".2f"))
print(format(5789.4, "<.2f"))
print(format(5789.4, ">9.2f"))

print(format(0.457657647, "9.3%"))
print(format(0.457467657, "<9.3%"))

print(format(45, "5d"))
print(format(45, "<5d"))
print(format(45, "5x"))
print(format(45, "<5x"))

print(format("Programing is fun", "25s"))
print(format("Programing is fun", "<25s"))
print(format("Programing is fun", ">25s"))

