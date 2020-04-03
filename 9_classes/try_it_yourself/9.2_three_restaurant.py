"""
Problem:
Start with your class from Exercise 9-1. Create three different instances from 
the class, and call describe_restaurant() for each instance.
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

restatrant_obj1 = Restaurant('the punjabi rosai', 'punjabi')
restatrant_obj1.describe_restaurant()

restatrant_obj2 = Restaurant('anand', 'north indian')
restatrant_obj2.describe_restaurant()

restatrant_obj3 = Restaurant('ghar ka khana', 'south indian')
restatrant_obj3.describe_restaurant()
