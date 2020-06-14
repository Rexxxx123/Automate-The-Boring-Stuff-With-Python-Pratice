# Dictionaries an Structuring Data
# The Dictionary Data Type
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

#dictionaries vs. lists
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
print(eggs == ham)

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

spam = {'color': 'red', 'age': 42}
spam.keys()
list(spam.keys())

# Checking whether a key or value exists in a dictionary
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)

# the get() method
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' cups.')

# the setdefault() method
spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#   spam['color'] = 'black'
spam.setdefault('color', 'black')


#Nested Dictionaries and Lists
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol':{'cups': 3, 'apple pies':1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples                 ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                   ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes                  ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches         ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies             ' + str(totalBrought(allGuests, 'apple pies')))



