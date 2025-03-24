"""This code keeps asking the user to enter a sea level until the user types "terminate". The code will then find the average sea level based on those inputs"""

# List
sea_level_list = []

# Constants


# Loop
while True:
    try:
        sea_level = input("Enter a sea level: ")
        if sea_level == "terminate":
            break
        sea_level = float(sea_level)
        if sea_level < 0:
            print("Please enter a positive number")
        else:
            sea_level_list.append(sea_level)
    except ValueError:
        print("Invalid!")