print([1, 2, 3])
print(['cat', 'dog', 'rat', 'elephant'])
print('Hello', 3.1415, True, None, 42)
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[0])
print(spam[3])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello ' + spam[0])
spam = [['cat', 'dog'], [10, 20, 30, 40]]
print(spam[0])
print(spam[1][3])
print(spam[-1])

#get sublist with slices
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[1:])
print(spam[:3])
print(spam[:])
print(spam[1:4])
print(spam[0:3])
print(spam[0:4])

#get a list's length by len()
spam = ['cat', 'bat', 'rat', 'elephant']
print(len(spam))

#change values in a list with indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'adshfalsd'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 3.1415
print(spam)

#List concatenation and list replication
print([1, 2, 3]+ ['a', 'b', 'c'])
print(['a', 'b', 'c'] * 3)
spam = [1, 2, 3]
print(spam + ['a', 'b', 'c'])

#Removing values from lists with del Statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

#using for loop with lists
for i in range(4):
    print(i)

for i in [0,1,2,3]:
    print(i)

supplies = ['pen', 'staplers', 'flam-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' +supplies[i] )

#in and not in operators
spam = ['hello', 'hi', 'howdy', 'heyas']
print('hi' in spam)
print('heyas' not in spam)
print('cats' not in spam)

#the multiple assignment trick
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)

#argumented assignment operators
spam = 42
spam += 1
print(spam)

spam = 'Hello'
spam += ' World!'
print(spam)

spam *= 3
print(spam)

#finding a value in a list with the index() method
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hi'))
print(spam.index('heyas'))

#adding values to lists with the append() and inser() method
spam =['cat', 'dog', 'bat']
spam.append('mouse')
print(spam)
spam.insert(1,'pig')
print(spam)

#remove values from lists with remove()
spam =['cat', 'dog', 'bat', 'rat']
spam.remove('dog')
print(spam)

#sort values with sort()
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['cat', 'pig', 'dog', 'bat', 'mouse']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam=['a', 'c', 'E', 'A', 'Z', 'x']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
