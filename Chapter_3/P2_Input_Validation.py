def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
    print('Amazing!')

try:
    collatz(int(input('Enter a Number: ')))
except:
    print('Please input an integer')