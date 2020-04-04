# inheritance - second class will take all the attributes and methods of the first class
# original class - parent class - superclass
# new class - child class - subclass
# Parent class must appear before child class

# PARENT CLASS
class Car():
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        '''Initialize attribute'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # Setting default value


    def get_descriptive_name(self):
        '''return formatted description'''
        long_name = str(self.year) +" "+ self.make +" "+ self.model
        return long_name.title()

    
    def read_odometer(self):
        '''Print car mileage'''
        print("This car has "+ str(self.odometer_reading) +" miles on it.")


    def update_odometer(self, mileage):
        '''Set the odometer value'''
        # Verify that the new is grater than the previous one 
        # It cannot be roll back
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, mileage):
        '''adding mileage to odometer'''
        self.odometer_reading += mileage

    # Class Car End


# CHILD CLASS
class ElectricCar(Car):     # Passing the parent class 
    '''Represent Electric vehicle'''

    def __init__(self, make, model, year):
        '''Initialize the parent class attribute'''
        # super should be the first statement in the method
        # super() function make connection between parent and child class
        super().__init__(make, model, year)   
        self.battery_size = 70  # Adding child class attribute


    def describe_battery(self):     # describing child method
        '''Describing car battery'''
        print("This car has a "+ str(self.battery_size) +"-KWh battery")

    # Class ElectricCar End

my_tesla = ElectricCar('tesla', 'model s', '2018')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()