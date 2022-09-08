''' Finding the number of years and days '''

# Prompt user to enter the minutes
minutes = eval(input("Enter number of minutes: "))
''' Assume 1-year has 365 days '''
#Compute for years
minPerYear = 365 * 24 * 60
years = minutes // minPerYear

#Compute for days
minPerDay = 24 * 60
daysLeft = minutes % minPerYear
days = daysLeft // minPerDay

# Display the number of years and days for the minutes
print(f'{minutes} minutes is approximately {years} years and {days} days')