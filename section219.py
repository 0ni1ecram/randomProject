''' Calculate Future investment value '''

# Read an investment amount
investmentAmount = eval(input("Insert the investment amount: "))

# Annual interest rate
annualIntrestRate = eval(input("Insert the annual interest rate: "))
monthlyIntrestRate = annualIntrestRate / 1200

# Number of years
noOfYears = eval(input("Insert the number of years: "))
numberOfMonths = noOfYears * 12

# Compute future investment value
futureInvestmentValue = investmentAmount * (1 + monthlyIntrestRate) ** numberOfMonths

# Display the Future investment value
print("Accumulated value is", futureInvestmentValue)