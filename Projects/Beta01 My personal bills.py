def plus(budget, bills):
    return budget + bills

def minus(budget, bills):
    return budget - bills

def times(budget, bills):
    return budget * bills

def div(budget, bills):
    return budget / bills

while True:
    print("Choose the operation for your bills")
    print("Adding the bills")
    print("Subracting the bills")
    print("Mulitiplying bills")
    print("Dividing the bills")

    chosen_operation = input("Enter chosen operation (+, -, x, /): ")

    if chosen_operation in ('+', '-', '*', '/'):
        weekly_budget = float(input("Enter your weekly budget here: "))
        bills = float(input("Enter the cost of bills: "))

        if chosen_operation == '+':
            print(weekly_budget, "+", bills, "=", plus(weekly_budget, bills))

        elif chosen_operation == '-':
            print(weekly_budget, "-", bills, "=", minus(weekly_budget, bills))
        
        elif chosen_operation == '*':
            print(weekly_budget, "x", bills, "=", times(weekly_budget, bills))
        
        elif chosen_operation == '/':
            print(weekly_budget, "/", bills, "=", div(weekly_budget, bills))
        break

