password = input('Enter a password: ')
while len(password) < 5:
    print('No, this password is not good enough.')
    password = input('Enter a password: ')
print('Thank you, your password is good enough.')