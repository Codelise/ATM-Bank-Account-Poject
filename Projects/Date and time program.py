import datetime

print("THIS IS A DATE AND TIME PROGRAM TELLER")

while True:
    clay_time = datetime.datetime.now()
    in_time = input("Wanna know the time today? Y/N: ")
    if in_time.upper() == "Y":    
        print("Today is",datetime.datetime.strftime(clay_time, '%H:%M'))
    elif in_time.upper() == "N":
        print("You're an expert!")
    elif in_time.upper() != "Y" and in_time.upper() != "N":
        print("Then what the hell do you want? ")
    else:
        print("You're on your own")
        break

    clay_date = datetime.date.today()
    in_date = input("Do you want to know the current date today? Y/N ")
    if in_date.upper() == "Y":
        print("Today is",clay_date.strftime('%b %d, %Y'))
        break
    elif in_date.upper() == "N":
        print("You're an expert!")
    elif in_date.upper() != "Y" and in_date.upper() != "N":
        print("Then what the hell do you want? ")
    else:
        print("You're on your own")
    
print("Thanks for trying this fun program! \nHave a nice day!")