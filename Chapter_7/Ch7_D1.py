# Creating Regex Objects
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# Matching multiple groups with the pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventure of Batwoman')
print(mo1.group())
print(mo2.group())

# Matching zero or mo0re with the star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventure of Batwoman')
mo3 = batRegex.search('The adventure of Batwowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())

# Matching one or mo0re with the star
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventure of Batwoman')
mo2 = batRegex.search('The adventure of Batwowowoman')
print(mo1.group())
print(mo2.group())
mo3 = batRegex.search('The adventures of Batman')
print(mo3 == None)

heRegex = re.compile(r'(Ha){3}')
mo1 = heRegex.search('HaHaHa')
print(mo1.group())
mo2 = heRegex.search('Ha')
print(mo2 == None)

# Greedy and nongreedy matching
heRegex = re.compile(r'(Ha){3,5}')
mo1 = heRegex.search('HaHaHaHaHa')
print(mo1.group())

heRegex = re.compile(r'(Ha){3,5}?')
mo2 = heRegex.search('HaHaHaHaHa')
print(mo2.group())

# The findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# Character Classes
xmaxRegex = re.compile(r'\d+\s\w+')
print(xmaxRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# Making your own character classes
vowelRegex= re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

consonantRegex= re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# the ^ and $ sign characters
beginsWithHello = re.compile(r'^Hello')
endsWithNumber = re.compile(r'\d$')
wholeStringIsNum = re.compile(r'^\d+$')

# the wildcard character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Matching Everything with dot-star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
greedyRegex = re.compile(r'<.*>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nPtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nPtect the innocent.\nUphold the law.').group())

# case-insensitive matching
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part an, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

# substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.'))