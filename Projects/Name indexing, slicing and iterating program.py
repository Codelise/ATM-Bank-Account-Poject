print("**********FIRST PROGRAM*********")
enter = input("Type your name here: ")
print("Your name will be indexed: " +enter[2])
print("Your name will be sliced: " +enter[1:4])
for alpha in enter:
    print("Your name will be iterate: " +alpha)

print("*********PROGRAM OVER********")
print(" ")
print("**********SECOND PROGRAM**********")

my_name = input("Type your name here to make a sequence:  ")
for name in my_name:
    print("The sequence of letter in your name is: " +name)

print("**********MOVING TO THE NEXT PROGRAM*********")
print(" ")
print("**********THIRD PROGRAM**********")
slice = input("Enter your name here to sliced it: ")
print("The sliced letter is: " +slice[:2])
print("The sliced letter is: " +slice[1:3])
print("The sliced letter is: " +slice[-3:1])

print("**********THANKS FOR PLAYING**********")