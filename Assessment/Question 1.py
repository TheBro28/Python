"""This code keeps asking the user to enter a sea level until the user types "terminate". The code will then find the average sea level based on those inputs"""

# LISTS
# Lists used to keep track of all the user entered inputs that are equal to or above 0 (sea_levels), and a list to store all the values above the average value (above_average).
sea_levels = []
above_average = []

# CONSTANTS
# Constants used to remove any sort of magic number/string in the program, allowing for easy changes in future.
STOP_CODE = "terminate"
ZERO = 0

# LOOP
# Loops the code forever until the user inputs "terminate".
while True:
 # Used a "try:" to test the code for errors.
    try:
        sea_level = input("Enter a sea level: ")
        if sea_level == STOP_CODE:
            break
        sea_level = float(sea_level)
        if sea_level < ZERO:
            print("Please enter a positive number")
        else:
            sea_levels.append(sea_level)
    except ValueError:
        print("Invalid!")

# Calculate average
for sea_level in sea_levels:
    average = sum(sea_levels) / len(sea_levels)
print(f"The average sea level is {average}.")

# 
for sea_level in sea_levels:
    if sea_level > average:
        above_average.append(sea_level)
print("List of sea levels above average: ")
print(", ".join(map(str, above_average)))
    