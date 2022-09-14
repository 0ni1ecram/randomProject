# Population projection

# Prompt user to enter number of years
numberOfYears = eval(input("Insert the number of years population prediction: "))
# Assuming current populstion
initialPopulation = 312032486

# Compute the increase in population
numberOfDays = numberOfYears * 365
timeInDay = 24 * 3600
rateOfBirth = timeInDay // 7
rateOfDeath = timeInDay // 13
rateOfMigrantion = timeInDay // 45

finalPopulation = initialPopulation + ((rateOfBirth + rateOfMigrantion - rateOfDeath) * numberOfDays)

# Display the predicted population
print(f'The population in {numberOfYears} years is {finalPopulation}')