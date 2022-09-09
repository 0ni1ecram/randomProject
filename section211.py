''' Investment amount '''
# Deposit money into savings account for intrest
finalAccountValue = eval(input("Insert final account value speculated: "))

# Account with anuaal intrest rate
annualIntrestRate = eval(input("Insert the annual interest rate of the account: "))
monthlyIntrestRate = annualIntrestRate / (12 * 100)

numberOfYears = eval(input("Number of years: "))
numberOfMonths = numberOfYears * 12

# What amount you need to deposit to have 5000 in 3years
# Computing the amount needed
initialDepositAmount = finalAccountValue * ((1 + monthlyIntrestRate)**-numberOfMonths)

print("Initial deposit value is", initialDepositAmount)