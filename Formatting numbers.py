print("I have {0:d} cats".format(6)) # I have 6 cats
print("I have {0:3d} cats".format(6)) # I have   6 cats
print("I have {0:03d} cats".format(6)) # I have 006 cats
print("I have {0:.2f} cats".format(6)) # I have 6.00 cats
# inside the parenthesis can be any number

# Using str.format()
num = 3.14159
formatted = "The value of pi is {:.2f}".format(num)
print(formatted)  # Output: "The value of pi is 3.14"

# Using f-strings
formatted = f"The value of pi is {num:.2f}"
print(formatted)  # Output: "The value of pi is 3.14"


num = 42
formatted = format(num, "03d")  # Pad with leading zeros to three digits
print(formatted)  # Output: "042"
