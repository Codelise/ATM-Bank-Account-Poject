def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def times(x, y):
    return x * y

def div(x, y):
    return x / y

while True:
    print("Choose operation")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    selected = input("Enter selected operation (+, -, *, /): ")

    if selected in ('+', '-', '*', '/'):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if selected == '+':
            print(n1, "+", n2, "=", plus(n1, n2))
        
        elif selected == '-':
            print(n1, "-", n2, "=", minus(n1, n2))
        
        elif selected == '*':
            print(n1, "x", n2, "=", times(n1, n2))
        
        elif selected == '/':
            print(n1, "/", n2, "=", div(n1, n2))
        break
    else:
        print("Invalid Input")