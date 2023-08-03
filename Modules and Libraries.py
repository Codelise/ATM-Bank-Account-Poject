# Python has some built-in modules too. The math module provides data like the value of PI and methods for different math operations.

import math # importing the math module

print("The value of pi is ")
print(math.pi)

print("The square root of 16 is ")
print(math.sqrt(16))

 # We can find out the functionality a module has by using the help() instruction with the name of the module
 # between the parenthesis

import math

square = math.sqrt(16)

help(math)

# We're able to use multiple different modules in the same file by adding a comma between the modules we're importing.

import statistics, math 

diameters = [9, 7, 4, 6]
result = statistics.mean(diameters)
print(f"Mean diameter is {result}")

print("Value of pi is: ")
print(math.pi)

# We can use the keyword FROM to extract only the functionality we care about, like here with from math import pi.

from math import pi

print("Value of pi is: ")
print(pi)

# Libraries are collections of modules that help us save time when coding.

# PIP stands for Preferred Installer Program.