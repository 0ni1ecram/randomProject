''' Escape Sequence for spacial characters '''
import math

print("He said, \"John's program is easy to read\"")

''' Printing a new line '''
print("AAA", end= ' ')
print("BBB", end= '')
print("CCC", end= '***')
print("DDD")

radius = 3
print("The area is ", math.pi * radius * radius, end= ' ')
print("and diameter is", 2 * radius)

''' The str function '''
s = str(3.4) # Convert Float to string
print(s)

f = str(3) # Convert integer to string
print(f)


''' String concatination operator '''

message = "Welcome " + "to " + "Python"
print(message)

chapterNo = 3
s = print("Chapter " + str(chapterNo))
s

message += " and Python is fun"
print(message)

''' Reading strings from the console '''
# s1 = input("Enter string: ")
# s2 = input("Enter string: ")
# s3 = input("Enter string: ")
# print("S1 is " + s1)
# print("S2 is " + s2)
# print("S3 is " + s3)

''' Using the "ord" function '''
print(ord('1'))
print(ord('A'))
print(ord('B'))
print(ord("a"))
print(ord('b'))

print(chr(40))
print(chr(59))
print(chr(79))
print(chr(85))
print(chr(90))

''' Display character / and " '''
print("\\ & \"")

''' How to write a character in UNICODE '''
# By using the "\u4ED3" where the \u is the start followed by the HexaDecimal number if the character

''' Output when A is entered '''
x = input("Enter character: ")
ch = chr(ord(x) + 3)
print(ch)

''' Output if A and Z are entered '''
x = input("Enter character: ")
y = input("Enter character: ")
print(ord(x) - ord(y))

''' Fixing code: title = "Chapter" + 1 '''
title = "Chapter " + str(1)

''' Show result of the following '''
sum = 2 + 3
print(sum)
s = '2' + '3'
print(s)