# Step 1: Class Definition
# To create a class in Python, we use the class keyword followed by the class name and a colon :. 
# Inside the class block, we define the attributes and methods that belong to the class.
class Car: # class is a template or blueprint for creating objects.
    # Class attributes and methods go here


# Step 2: Class Attributes
# Class attributes are variables that belong to the class and are shared by all instances (objects) of the class.
# They represent data associated with the class. We define class attributes directly within the class, outside any methods.
class Car:
    # Class attribute
    car_type = "Automobile"

# Step 3: Constructor and Instance Attributes
# A constructor is a special method that initializes the instance (object) of the class. In Python, the constructor is defined using the __init__ method. 
# It is automatically called when we create an instance of the class.
# We use the constructor to set the initial values of instance attributes.
class Car:
    car_type = "Automobile"

    # Constructor
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year

# Step 4: Class Methods
# Class methods are functions that belong to the class and can operate on class attributes or perform specific actions related to the class.
# They are defined inside the class and take self as the first parameter, which represents the instance of the class.
class Car:
    car_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Class method
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Step 5: Instance Creation and Accessing Attributes and Methods
# To create an instance (object) of the class, we call the class like a function, passing the required arguments to the constructor.
# Each instance has its own set of attributes and can have unique values for those attributes.
# We can access the attributes and call methods using dot notation.
# Create an instance of the class
car1 = Car("Toyota", "Corolla", 2022)

# Access instance attributes
print(car1.make)  # Output: "Toyota"
print(car1.model)  # Output: "Corolla"
print(car1.year)  # Output: 2022

# Call class method
car1.display_info()  # Output: "Make: Toyota, Model: Corolla, Year: 2022"

# Now, let's put all the steps together and create the complete program:

class Car:
    car_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Create an instance of the class
car1 = Car("Toyota", "Corolla", 2022)

# Access instance attributes
print(car1.make)  # Output: "Toyota"
print(car1.model)  # Output: "Corolla"
print(car1.year)  # Output: 2022

# Call class method
car1.display_info()  # Output: "Make: Toyota, Model: Corolla, Year: 2022"
