"""This code asks the user to input a battery charge, if the charge is over or equal to 1.2, then it will print beep, if it is lower that 1.2 then it will print boop."""

# Used to store all charge numbers the user imputs
charge_list = []
charged = 1.2

# Used "try" to test code for invalid inputs
# Asks the user for an input, and adds it into the charge_list, repeats until the user inputs -1. If the use inputs a value that is less than -1 it will break the loop.
try:
    charge = float(input("Enter your input: "))
    while charge >= 0:
        charge_list.append(charge)
        charge = float(input("Enter your input: "))
        if charge < 0:
            break
# If the user inputs a value that is not a number, it will print "Not robot compliant!"
except ValueError:
    print("Not robot compliant!")

# Prints out the list of charges, and if the charge is over or equal to 1.2, it will print "Beep", if it is lower than 1.2, it will print "Boop"
for charge in charge_list:
    if charge >= charged:
        print("Beep")
    else:
        print("Boop")