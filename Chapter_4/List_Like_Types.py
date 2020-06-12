name = 'Zophioe'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('p' not in name)
for i in name:
    print('***' + i + '***')

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

#the tuple data type
eggs =('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

#convert types with the list() and tuple() functions
print(tuple(['cat', 'dog', 'bat']))
print(list(('cat', 'dog', 'bat')))
print(list(('Hello')))

