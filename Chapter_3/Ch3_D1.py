def hello():
    print('Howdy!')
    print("Howdy!!")
    print('Hello there.')

hello()
hello()
hello()

def hello(name):
    print('Hello ' + name)
hello('Alice')
hello('Bob')

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is Certain'
    elif answerNumber == 2:
        return 'It is Decidedly so'
r = random.randint(1,2)
fortune = getAnswer(r)
print(fortune)

print('Hello')
print('World')

print('Hello', end='')
print('World')

print('cat', 'dog', 'mice')
print('cat', 'dog', 'mice', sep=',')

def spam():
    eggs=99
    bacon()
    print(eggs)
def bacon():
    hum=101
    eggs=0
spam()

def spam():
    print(eggs)
eggs=42
spam()
print(eggs)