"""This code keeps asking the user to enter a sea level until the user types "terminate". The code will then find the average sea level based on those inputs"""

# Lists used to keep track of all the user entered inputs that are equal to or above 0 (sea_levels), and a list to store all the values above the average value (above_average).
sea_levels = []
above_average = []

# Constants used to remove any sort of magic number/string in the program, allowing for easy changes in future.
STOP_CODE = "terminate"
ZERO = 0
ONE_ABOVE_AVERAGE = 1

# Loops the code forever until the user inputs "terminate".
while True:
 # Used a "try:" to test the code for errors.
    try:
 # Asks the user for an input, if the input is "terminate it will break the loop. 
 # If that condition is not met then it changes the input to a float, causing any other strings that aren't "terminate" to be picked up Except ValueError block.
 # If the input is a negitave number it will ask the user to input a positive number.
  # If the input is then found to be a number it will add the input to the "sea_levels" list.
        sea_level = input("Enter sea level: ")
        if sea_level == STOP_CODE:
            break
        sea_level = float(sea_level)
        if sea_level < ZERO:
            print("Please enter a positive number!")
        else:
            sea_levels.append(sea_level)
# Value Error picks up any string inputs that aren't "terminate", outputs invalid, then repeats the question.
    except ValueError:
        print("Invalid!")

# Used a for loop to go through all the appended values in the "sea_levels" list.
# Calculates the average by adding the sum of all the numbers in the list "sum(sea_levels)", divided by how many items are in the list "len(sea_levels)". Prints out the average sea level.
for sea_level in sea_levels:
    average = sum(sea_levels) / len(sea_levels)
print(f"The average sea level is {average}.")

# For loop goes through all the sea levels in the "sea_levels" list. If the a sea level in that list is greater than the average sea level then that value will be added to the "above_average" list.
# Prints out the sea levels above the average sea level ONE LINE AFTER THE OTHER.

for sea_level in sea_levels:
    if sea_level > average:
        above_average.append(sea_level)
if len(above_average) >= ONE_ABOVE_AVERAGE:
    print("List of sea levels above average: ")
    for i in above_average:
        print(i)
    