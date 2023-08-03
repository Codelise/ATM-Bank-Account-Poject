fileName = "demo.txt"
WRITE = "w"
APPEND = "a"
READ = "r"
BINARY = "b"

file = open(fileName, mode = WRITE) # this code open files
file.write("This is the first line \n")
file.write("This is the second line")
file.close()

 #open my file
animalFile = open("Tasmania.txt", "r")

firstAnimal = animalFile.readline() #read single line
print(firstAnimal)
secondAnimal = animalFile.readline()
print(secondAnimal)
#read all file contents
# allFileContents = animalFile.read()
# print(allFileContents)

#CSV Files

import csv

#open my file
with open("Tasmania.txt", "r") as animalFile:
    allRowsList = csv.reader(animalFile) #this converts into a list
  
    for currentRow in allRowsList:
        print(';'.join(currentRow)) #this removes the square brackets from the
