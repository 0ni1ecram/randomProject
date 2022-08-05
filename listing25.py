''' Display Time '''
# Prompt the user for input
sec = eval(input("Enter integer for seconds: "))

# Get Minutes and remaining seconds
minutes = sec // 60
remainingSec = sec % 60

print(sec, "seconds is", minutes, "minutes and", remainingSec, "seconds")

print("\n",2.3E4)
# Results of the following expressions
res1 = 42 / 5
res2 = 42 // 5
res3 = 42 % 5
res4 = 1 % 2
res5 = 2 % 1
res6 = 45 + 4 * 4 - 2
res7 = 45 + 43 % 5 * (23 * 3 % 2)
res8 = 5 ** 2
res9 = 5.1 ** 2

print(f'42 / 5 = {res1}\n 42 // 5 = {res2}\n 42 % 5 = {res3}\n 1 % 2 = {res4}\n 2 % 1 = {res5}\n 45 + 4 * 4 - 2 = {res6}\n \
45 + 43 % 5 * (23 * 3 % 2) = {res7}\n 5 ** 2 = {res8}\n 5.1 ** 2 = {res9}\n')

# What day of the week will it be in 100 days
DayAfterTuesday = 100 % 7
print(DayAfterTuesday, 'days after Tuesday\n')

# 25 / 4 in integer form
int = 25 //4
print("25 / 4 in integer form =",int)

