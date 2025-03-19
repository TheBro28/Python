"""This program asks the user to input the amount spent, it will then store the transactions in a list. After the user inputs 0, the code will print out the balance after each transaction."""

# Used list called "transaction_list" to store all the transactions the user inputs
transaction_list = []

# Used variables to store the balance and the stop value
STOP = 0
BALANCE = 200

# Used a "while True" loop to repeat the code over and over untill the user inputs 0. Also used a "try" to test code for invalid inputs
# Asks the user to input the amount spent, if the amount spent is over 0, it will add the amount to the list. If the user inputs 0 it will break the loop and print out the balance after each transaction. If the user inputs a value that is less than 0 it will add the value to the list.
# If the total amount spent is over or equal to the balance, it will break the loop
while True:
    try:
        money = int(input('Enter the amount spent: '))
        if money == STOP:
            break
        elif money >= BALANCE:
            transaction_list.append(money)
            break
        elif money > STOP:
            transaction_list.append(money)
        if sum(transaction_list) >= BALANCE:
            break
    except ValueError:
        print('That is not a valid transaction.')

# Prints out the balance after each transaction
print("My bank balances have been:")
print(BALANCE)
for money in transaction_list:
    BALANCE -= money
    print(BALANCE)