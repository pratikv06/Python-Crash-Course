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


    # Class End

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n>> Updating odometer value to 50")
my_new_car.update_odometer(50)
my_new_car.read_odometer()

print("\n>> Updating odometer value lower than previous value")
my_new_car.update_odometer(25) # Assigning a lower value
my_new_car.read_odometer()

# This is also possible while updating a value, 
# but using a method is best practice
# 
# SYNTAX:
# my_new_car.odometer_reading = 100
# my_new_car.read_odometer()

print("\n>> Incrementing odometer value by 150")
my_new_car.increment_odometer(150)
my_new_car.read_odometer()
