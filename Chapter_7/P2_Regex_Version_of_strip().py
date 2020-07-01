def stripRegex(s,character=None):
    import re
    if character is None:
        character = '\s'
    return re.sub(r'^[{0}]+|[{0}]+$'.format(character), '', s)


x1 = ''
x2 = 'ampS'
x3 = 'mapS'
x4 = 'Spam'
string1 = '      Hello world   '
string2 = 'SpamSpamBaconSpamEggsSpamSpam'

print(stripRegex(string1))  # 'Hello world!!!'
print(stripRegex(string1, x1))  # '      Hello world!!!   '
print(stripRegex(string2, x2))  # 'BaconSpamEggs'
print(stripRegex(string2, x3))  # 'BaconSpamEggs'
print(stripRegex(string2, x4))  # 'BaconSpamEggs'