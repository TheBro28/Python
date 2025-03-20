"""This code asks the user to input a score"""
# 
PASS = 80
TOP_SCORE = 100
ZERO = 0
ONE_SMART_STUDENT = 1

# 
scores = []

# 
while True:
    try:
        score = input("Enter a score, or type 'done' to exit: ")
        if score == 'done':
            break
        score = int(score)
        if score >= PASS and score <= TOP_SCORE:
            scores.append(score)
        elif score < ZERO:
            print("Please type a positive number.")
    except ValueError:
        print("Please type a number.")

#
for score in scores:
    if len(scores) == ONE_SMART_STUDENT:
        print(f"This class has 1 smart student!")
        break
    else:
        print(f"This class has {len(scores)} smart students!")
        break

