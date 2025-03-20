"""This code asks the user to input a score, it will then store the scores in a list and print out the amount of smart students in the class."""

# Used constants to store the pass mark, top score, one, and zero.
PASS = 80
TOP_SCORE = 100
ZERO = 0
ONE = 1

# Used a list to store all the scores the user inputs.
scores = []

# Used a while true loop to repeat the code forever untill the user inputs 'done'.
# Used a try to test code for invalid inputs.
# Asks the user to input a score, if the score is over or equal to 0 and under or equal to 100, it will add the score to the list. If the user inputs a value that is less than 0 it will print "Please type a positive number."
while True:
    try:
        score = input("Enter a score, or type 'done' to exit: ")
        if score == 'done':
            break
        score = int(score)
        if score >= ZERO and score <= TOP_SCORE:
            scores.append(score)
        elif score < ZERO:
            print("Please type a positive number.")
    except ValueError:
        print("Invalid score!")

# Checks if the score is over or equal to the pass mark, if it is, it will add one to the smart_students variable.
smart_students = ZERO
for score in scores:
   if score >= PASS:
        smart_students += ONE

# Prints out the amount of smart students in the class.
if smart_students == ONE:
    print("This class has 1 smart student!")
else:
    print(f"This class has {smart_students} smart students!")

