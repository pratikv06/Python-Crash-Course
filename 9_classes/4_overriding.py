# define a method in child class with the same name as the method you want to 
# override in the parent class

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


    def fill_gas_tank(self):
        '''display that gas tank is less than 10%'''
        print("Please, refill the tank!")

    # Class Car End


# CHILD CLASS
class ElectricCar(Car):     # Passing the parent class 
    '''Represent Electric vehicle'''

    def __init__(self, make, model, year, battery):
        '''Initialize the parent class attribute'''
        # super should be the first statement in the method
        # super() function make connection between parent and child class
        super().__init__(make, model, year)   
        self.battery_size = battery # Adding child class attribute


    def describe_battery(self):     # describing child method
        '''Describing car battery'''
        print("This car has a "+ str(self.battery_size) +"-KWh battery")


    def fill_gas_tank(self):  # Comment this method to call parent class method
        '''display that gas tank is less than 10%'''
        print("This car doesn't need a gas tank!")

    # Class ElectricCar End

my_tesla = ElectricCar('tesla', 'model s', 2018, 70)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()