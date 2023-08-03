class Car:
    def start_car(self):
        print("Starting the car")
class Hybrid(Car): # Passing the Car class inside the Hybrid Class
    def charge(self):
        print("Using fuel to charge battery")
prius = Hybrid() #Calls out the Hybrid class
prius.start_car() # Calls out the def start_car method
prius.charge() #Calls out the def charge method