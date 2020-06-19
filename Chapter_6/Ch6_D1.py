# Manipulating Strings
spam = "That is Alice's cats"
print(spam)
spam = 'Say hi to Bob\'s mother'
print(spam)
print("Hello there!\nHow are you?\nI\'m doing fine.")

# raw strings
print(r'That is Carol\'s cat.')

# multiple strings with triple quotes
print('''Dear Alice,

how are you

Thank you,
Bob''')

print('''Dear Alice,\n\nhow are you\n\nThank you,\nBob''')

#indexing and slicing strings
spam = 'Hello World'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
spam = 'Hello world!'
fizz = spam[0:5]
print(fizz)

# the in and not in operators with strings
print('Hello' in 'Hello World')
print('Hello' in 'Hello')
print('HELLO' in 'Hello World')
print('' in 'spam')
print('cats' not in 'cats and dogs')

# Useful String Methods
spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)


# the upper(), lower(), isupper(), and islower() string methods
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

spam = 'Hello world!'
print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())

#The isX String Methods
print('hello'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('   '.isspace())
print('This is title'.istitle())
print('This Is Title'.istitle())

# the startwith() and endwith() string methods
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))
print('abc123'.endswith('12'))
print('Hello world!'.startswith('Hello world!'))

# the join() and split() string methods
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join((['My', 'name', 'is', 'Simon'])))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))

# Justifying Text with rjust(), ljust(), and center()
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(10,'*'))
print('Hello'.ljust(10,"#"))
print('Hello'.center(20))
print('Hello'.center(20,'-'))

# removing whitespace with strip(), rstrip(), and lstrip()
spam = '      Hello World    '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))  #spam.strip('mpaS') order of the characters in the string passed to strip() does not matter

# copying and pasting strings with the pyperclip module
import pyperclip
pyperclip.copy('Hello World!')
print(pyperclip.paste())

