import re
PasswordRegex = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}')

def StrongPass(password):
    while True:
        if not PasswordRegex.search(password):
            print('This is not a strong password')
            print('Please enter a new password: ')
            password = input()
        else:
            break
    print('This is a strong password')

password = input()
print(StrongPass(password))