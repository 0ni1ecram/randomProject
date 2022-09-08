''' Compute Loan '''

# Enter interest rate as percentage
annualInterestRate = eval(input("Enter annual interest rate(eg.7.23): "))
monthlyInterestRate = annualInterestRate / 1200

# Enter Number of years
numberOfYears = eval(input("Enter number of years(eg.4): "))

# Enter loan amount
loanAmount = eval(input("Loan amount: "))

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate/(1 - ((1+monthlyInterestRate)**(-12*numberOfYears)))
totalPayment = monthlyPayment * numberOfYears * 12

# Display Result
print("Monthly payment is:", int(monthlyPayment*100)/100)
print("Total payment is:", int(totalPayment*100)/100)
