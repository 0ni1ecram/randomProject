''' Sum the digits in an integer '''

# Read an int between 0 to 1000
int = eval(input("Write an integer between 0 and 1000: "))
digit1 = int // 100     # Getting the first digit
subint = int //10       # Reducing the int to 2-digit number
digit2 = subint % 10    # Getting the middle value
digit3 = int % 10       # Getting the last digit

# Add all digits
sum = digit1 + digit2 + digit3

# Result
print("Sum of digits is:", sum)