"""This program will ask the user for their name and favourite number and then preform some simple maths on the numbers"""

#Ask the user for their name and favourite numbers
name = input('What is your name? ')
num1 = int(input('What is your favourite number? '))
num2 = int(input('What is your second favourite number? '))

#perform some math on the number
add = num1 + num2
multiply = num1 * num2


#greet the user and print the results
print(f"Hi {name}, here are some fun calculations with your favourite numbers:")
print(f'{num1} + {num2} = {add}')
print(f'{num1} x {num2} = {multiply}')
