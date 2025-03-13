""""This code asks the user to input a temperature, it will then store the temperatures in a list. After the user inputs -1, the code will check if the temperature is too cold, just right, or too hot."""

# Used variables to store the temperatures
COLD = 34
HOT = 42
ZERO = 0
STOP = -1

# Used list called "temp_list" to store all the temperatures the user inputs
temp_list = []

# Used a "while True" loop to repeat the code over and over untill the user inputs -1. Also used a "try" to test code for invalid inputs
# Asks the user to input a temperature, if the temperature is above or equal to 0, it will add the temperatures to the list, if the user inputs -1 it will break the loop. If the user inputs a value that is less than -1 it will add the value to the list.
while True:
    try:
        temp = int(input('Enter the temperature: '))
        if temp >= ZERO:
            temp_list.append(temp)
        elif temp == STOP:
            break
        else:
            temp_list.append(temp)

# Used "except ValueError" to print "Invalid temperature" if the user inputs a value that isn't a number
    except ValueError:
        print('Invalid temperature.')

# Used a for loop to check if the temperature is too cold, just right, or too hot, and print out the results
for temp in temp_list:
    if temp < COLD:
        print("too cold")
    elif temp >= COLD and temp <= HOT:
        print("just right")
    else:
        print("too hot")
