print("THIS IS MY PERSONAL MINI CALCULATOR PROJECT")

def plus(int1, int2):
    return int1 + int2

def minus(int1, int2):
    return int1 - int2

def times(int1, int2):
    return int1 * int2

def divide(int1, int2):
    if int2 == 0:
        return "Error: division by zero"
    else:
        return int1 / int2

def calcu():
    operation = input("Enter an operation +, -, x, / : ")
    int1 = float(input("Enter the first number: "))
    int2 = float(input("Enter the second numer: "))

    if operation == "+":
        result = plus(int1, int2)
    elif operation == "-":
        result = minus(int1, int2)
    elif operation == "x":
        result = times(int1, int2)
    elif operation == "/":
        result = divide(int1, int2)

    print(f"{int1} {operation} {int2} = {result}")

calcu()