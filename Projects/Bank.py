import random
 
bank_account_passcode = (40303, 3705, 1909, 911)
current_balance = [50000]
deposit = [500, 1000, 2000, 5000, 10000]
Addmoney = [500, 1000, 2000, 5000, 10000]

def balance():
    balance_str = " ".join(str(balance) for balance in current_balance)
    print(f"Your current balance is: ₱{balance_str}")

def withdraw(current_balance, draw):
    result = current_balance[0] - draw
    current_balance[0] = result

def deposit_money(current_balance, added_money):
    if added_money > 0:
        result = current_balance[0] + added_money
        current_balance[0] = result
    else:
        print("Invalid deposit amount. Please enter a positive value.")

while True:
    pin = int(input("Enter your pin: "))
    if pin in bank_account_passcode:
        print("Access Granted!")
        break
    else:
        print("Wrong pin number!")

while True:
    user = input("Would you like to (View Balance / Withdraw / Add): ").lower()
    if user == "view":
        balance()
        continue
    elif user == "withdraw":
        for value in deposit:
            print(value)
        draw = int(input("Choose the amount you would like to withdraw: "))
        if draw in deposit:
            if draw <= current_balance[0]:
                withdraw(current_balance, draw)
                print(f"Withdrawn ₱{draw}. Remaining balance: ₱{current_balance[0]}")
                break
            else:
                print("Insufficient balance. Please choose a lower amount.")
        else:
            print("Invalid withdrawal amount. Please choose from the available options.")
    elif user == "add":
        for val in Addmoney:
            print(val)
        added_money = int(input("Enter the amount you would like to add: "))
        deposit_money(current_balance, added_money)
        print(f"Added ₱{added_money}. Your new balance is: ₱{current_balance[0]}")
        break
    else:
        print("Invalid input. Please enter 'View', 'Withdraw', or 'Add'.")
        

print("Please take your card")