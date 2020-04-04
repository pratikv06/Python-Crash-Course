"""
Problem:
Use the final version of electric_car.py from this section. Add a method to the 
Battery class called upgrade_battery(). This method should check the battery 
size and set the capacity to 85 if it isn’t already. Make an electric car with 
a default battery size, call get_range() once, and then call get_range() a 
second time after upgrading the battery. You should see an increase in the car’s 
range.
"""

# PARENT CLASS
class Car():
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        '''Initialize attribute'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   


    def get_descriptive_name(self):
        '''return formatted description'''
        long_name = str(self.year) +" "+ self.make +" "+ self.model
        return long_name.title()

    
    def read_odometer(self):
        '''Print car mileage'''
        print("This car has "+ str(self.odometer_reading) +" miles on it.")


    def update_odometer(self, mileage):
        '''Set the odometer value'''
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


# CLASS BATTERY
class Battery():
    '''A simple attempt to model a battery for an  Electric car '''

    def __init__(self, battery):
        '''Initialize attribute'''
        self.battery_size = battery


    def describe_battery(self):    
        '''Describing car battery'''
        print("This car has a "+ str(self.battery_size) +"-KWh battery.")


    def get_range(self):
        '''Print range of the battery'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print("This car can go approximately "+ str(range) +" miles on a full charge.")


    def upgrade_battery(self):
        '''upgrade battery to 85'''
        if self.battery_size != 85:
            self.battery_size = 85
            print("battery Upgraded!")

    # Class Battery End


# CHILD CLASS
class ElectricCar(Car):    
    '''Represent Electric vehicle'''

    def __init__(self, make, model, year, battery=70): 
        '''Initialize the parent class attribute'''
        super().__init__(make, model, year)   
        self.battery = Battery(battery) 


    def fill_gas_tank(self):  
        '''display that gas tank is less than 10%'''
        print("This car doesn't need a gas tank!")

    # Class ElectricCar End

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()    
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()    
