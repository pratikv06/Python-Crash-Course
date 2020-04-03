"""
Problem:
Start with your program from Exercise 9-1. Add an attribute called number_served 
with a default value of 0. Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this 
value and print it again.
Add a method called set_number_served() that lets you set the number of 
customers that have been served. Call this method with a new number and print 
the value again.
Add a method called increment_number_served() that lets you increment the number 
of customers who’ve been served. Call this method with any number you like that
could represent how many customers were served in, say, a day of business.
"""

class Restaurant():
    """Describe restaurant name and cuisine thet provide"""

    def __init__(self, name, cuisine):
        """Initializing restaurant name and cuisine attribute"""
        self.restuarant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    
    def describe_restaurant(self):
        """Display information about restuarant"""
        print("Name of the Restaurant name is : "+ self.restuarant_name.title())
        print("Type of cuisine they provide is : "+ self.cuisine_type.title())

    
    def get_served_number(self):
        '''display total number of dish served'''
        print("Total number of customer served is : "+ str(self.number_served))

    
    def set_number_served(self, served):
        '''Update number of served dish'''
        self.number_served = served


    def increment_number_served(self, increment_served):
        '''increment served dish by increment_served'''
        self.number_served += increment_served

    # Class End


restaurant_obj = Restaurant('the punjabi rosai', 'punjabi')
restaurant_obj.describe_restaurant()
restaurant_obj.get_served_number()

print("\n>> Updating value of dish served to 18")
restaurant_obj.set_number_served(18)
restaurant_obj.get_served_number()

print("\n>> Incrementing the dish served by 5")
restaurant_obj.increment_number_served(5)
restaurant_obj.get_served_number()
