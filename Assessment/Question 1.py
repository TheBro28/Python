"""This code keeps asking the user to enter a sea level until the user types "terminate". The code will then find the average sea level based on those inputs"""

# List
sea_levels = []
above_average = []

# Constants
STOP_CODE = "terminate"
ZERO = 0

# Loop
while True:
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
print(above_average)
