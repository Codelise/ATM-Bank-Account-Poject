# In Object Oriented Programming(OOP), we group data and functionality as properties and methods inside objects, like Virtual_per() here.

class Virtual_Pet:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
rocky = Virtual_Pet("brown", "rocky")

print(rocky.color)
print(rocky.name)

# We can update how classes work by setting methods directly in the class.
# Define the CHARGE method inside the Hybrid class.

class Car:
    def start_car(self):
        print("Starting the car")
class Hybrid(Car): # Passing the Car class inside the Hybrid Class
    def charge(self):
        print("Using fuel to charge battery")
prius = Hybrid() #Calls out the Hybrid class
prius.start_car() # Calls out the def start_car method
prius.charge() #Calls out the def charge method

# INHERITANCE
# We can use the concept of inheritance to reuse parts of code in our classes, 
# making our code more readable and efficient.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hi!")

class Nurse(Person):
    def __init__(self, name, age):
        super().__init__("Nurse " + name, age) # The super().__init__() allows us to access the class Person 
    def intro(self):
        print("Hi, I'm", self.name)

person1 = Nurse("Sam", 23) # 
person2 = Person("Tom",30)

# super().__init__() refers to Student's parent class, Person.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hi!")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major 

student = Student("Sam", 23, "chemistry")
print(student.major)
student.greet()

# ABSTRACTION
# Abstraction allow other developers to use a class without having to know what low-level methods it has or how they even work.

class Coffeemaker:
    def heatWater(self):
        print('Heating water')

    def brew(self):
        print('Adding water to grounds')

    def filterCoffee(self):
        print('Filtering coffee')

    def makeCofee(self):
        self.heatWater()
        self.brew()
        self.filterCoffee()

coffeeMaker = Coffeemaker()
coffeeMaker.makeCofee()

# POLYMORPHISM
# Ensures that the proper method will be executed based on the calling object's class.

class Feline:
    def speak(self):
        print("Meow")
    
class Cat(Feline):
    def lick(self):
        print("Licking paw")

class Lion(Feline):
    def prey(self):
        print("Pounces on prey")
    def speak(self):
        print("ROAR!")

cat = Cat()
cat.speak()
lion = Lion()
lion.speak()
