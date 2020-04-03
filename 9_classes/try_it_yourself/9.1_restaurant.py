"""
Problem:
Make a class called Restaurant. The __init__() method for  Restaurant should 
store two attributes: a restaurant_name and a cuisine_type. Make a method called 
describe_restaurant() that prints these two pieces of information, and a method 
called open_restaurant() that prints a message indicating that the restaurant
is open. Make an instance called restaurant from your class. Print the two
attributes individually, and then call both methods.
"""

class Restaurant():
    """Describe restaurant name and cuisine thet provide"""

    def __init__(self, name, cuisine):
        """Initializing restaurant name and cuisine attribute"""
        self.restuarant_name = name
        self.cuisine_type = cuisine

    
    def describe_restaurant(self):
        """Display information about restuarant"""
        print("Name of the Restaurant name is : "+ self.restuarant_name.title())
        print("Type of cuisine they provide is : "+ self.cuisine_type.title())

    
    def open_restaurant(self):
        """Dispaly restuarant is open"""
        print("Resturant `"+ self.restuarant_name.title() +"` is open!" )

    # Class End

restaurant_obj = Restaurant('the punjabi rosai', 'punjabi')
restaurant_obj.describe_restaurant()
restaurant_obj.open_restaurant()