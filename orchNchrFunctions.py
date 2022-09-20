''' The ord and chr '''

ch = 'a'
ord(ch)

chr(98)
ord('A')

offset = ord('a') - ord('A')


lowercaseLetter = 'h'
uppercaseLetter = chr(ord(lowercaseLetter) - offset)
a = uppercaseLetter
print(a)
