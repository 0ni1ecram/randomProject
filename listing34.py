# Program: Classifies money into monetary amounts
#  User enters ammount as a floating point
amount = eval(input("Insert value in decimal: "))
# Compute amount into cents
cent = amount * 100

# Compute number of dollars
dollars = cent // 100
cents = cent % 100

# Compute Quaters
quaters = cents // 25
cents = cents % 25

# Compute Dimes
dimes = cents // 10
cents = cents % 10

# Compute Nickels
nickels = cents // 5
cents = cents % 5

# Pennies
cents

# Output: monetary equivalent to dollars, no. of quaters, dimes, nickles n pennies
print(f'Your amount {amount} consists of \n\t {dollars} dollars \n\t {quaters} quaters \n\t {dimes} dimes \n\t {nickels} nickels \n\t {cents} cents')