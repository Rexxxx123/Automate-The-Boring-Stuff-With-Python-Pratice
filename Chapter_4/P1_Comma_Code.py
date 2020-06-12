def CommaCode(spam):
    if len(spam) > 2:
        for i in range(len(spam)-2):
            print(spam[i] + ', ', end='')
        else:
            print(spam[-2] + ' and ' + spam[-1])
    elif len(spam) == 2:
        print(spam[0] + ' and ' + spam[1], end='')
    else:
        print(spam[0])

