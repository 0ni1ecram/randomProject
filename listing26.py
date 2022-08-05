''' Sales Tax'''
#Prompt user for input
import time

purchaseAmount = eval(input("Enter purchase amount: "))

# Compute sales Tax
tax = purchaseAmount * 0.06

# Display tax amount with two digits after decimal places
print("Sales tax is", int(tax * 100) / 100.0)

print(eval("4*5+2"))
