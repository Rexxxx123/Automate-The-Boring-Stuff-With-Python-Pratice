print(42 == 42)
print(42 == 99)
print(2 != 3)
print(2 !=2)
print( 'hello' == 'hello')
print('hello' == 'Hello')
print('Dog' != 'Cat')
print(True == True)
print(True != False)
print(42 == 42.0)
print(42 == '42')
myage = 29
print(myage >= 10)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or False)
print(not True)

#------------------------------------
# if name == 'Mary':
#     print('Hello Mary')
#     if password == 'swordfish':
#        print('Access Granted.')
#     else:
#        print('Wrong Password.')

# if name == 'Alice':
#   print('Hello Alice')
# elif age < 12:
#    print('You are not Alice, Kiddo')
# elif age > 2000:
#    print('Unlike you, Alice is not an undead, immortal vampire')
# elif age > 100:
#    print('You are not Alice, grannie.')

spam=0
if spam < 5:
    spam = spam + 1
    print(spam)

spam=0
while spam < 5:
    spam = spam + 1
    print(spam)

name = ''
while name != 'Your Name':
    print('Please type your name.')
    name = input()
print('Thank you!')

while True:
    print('Please type your name.')
    name = input()
    if name == 'Your Name':
        break
print('Thank you!')

for i in range(12, 16):
    print(i)

import random
for i in range(5):
    print(random.randint(1,10))