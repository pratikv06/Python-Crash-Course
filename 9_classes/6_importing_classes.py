# Import all module from class
# from module_name import *
# Importing multiple classes
from car import Car, ElectricCar


my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_beetle.read_odometer()

print()
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()