''' Compound Value '''

# Promp user to enter savings amount
savingsAmount = eval(input("Insert the monthly saving amount: "))

# Compute account value, monthly intrest rate is 5%
x = (1 + 0.00417)
accountValue = 0
y = ((savingsAmount + accountValue) * x)
y1 = ((savingsAmount + y) * x)
y2 = ((savingsAmount + y1) * x)
y3 = ((savingsAmount + y2) * x)
y4 = ((savingsAmount + y3) * x)
y5 = ((savingsAmount + y4) * x)

# Display amount after 6-months
print("Account value after 6-months",y5)



