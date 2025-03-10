name = input('What is your name? ')
age = int(input(f'How old are you, {name}? '))
print(f'Hello {name}, aged {age}, nice to meet you!')

if age == 15:
    print(f'Great age {name}')
else:
    print(f'Maybe pick a better age next time, {name}')
    