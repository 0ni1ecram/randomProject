''' Calculate the Interest '''

# Prompt the balance and annual interestRate
balance = eval(input("Insert your balance: "))
annualIntrestRate = eval(input("Insert the intrest rate: "))

# Computing the interest in the next monthly payment
interest = balance * (annualIntrestRate / 1200)

# Display the answer
print("The interest is", interest)