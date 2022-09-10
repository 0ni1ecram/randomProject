''' Split Digits '''

# Prompt user to write 4-digit number
numb = eval(input("Insert 4-digit number: "))

# Compute the reverse order
revNum = (numb % 10)*1000 + ((numb // 10) % 10)*100 + ((numb // 100) % 10)*10 + (numb // 1000)
# print(numb % 10)
# print((numb // 10) % 10)
# print((numb // 100) % 10)
# print(numb // 1000)

# Print in reverse order
print(f"Reverse order of integer {numb}: {revNum}")