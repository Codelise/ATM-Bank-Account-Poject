import sys #if you want to know sys.exc_info error


#try and except
firstNumber = float(input("enter a number"))
secondNumber = float(input("enter a number"))

try: #if the result was error, it will immediately jump to  (except)
    result = firstNumber / secondNumber
    print(result)
#except: # if the code never runs an error, this won't run
except ZeroDivisionError: #It won't look like an error
    print("The answer is infinity")
    # error = sys.exc_info()[0] 
    # print(error)
    # print("I am sorry something went wrong")
finally: #it will always execute
    print("I will always run!!!")

#sys.exit() to exit the program if there's an error