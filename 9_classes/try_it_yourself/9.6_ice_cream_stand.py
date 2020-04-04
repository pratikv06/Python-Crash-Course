"""
Problem:
An ice cream stand is a specific kind of restaurant. Write a class called 
IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 
or Exercise 9-4. Either version of the class will work; just pick the one you 
like better. Add an attribute called flavors that stores a list of ice cream 
flavors. Write a method that displays these flavors. Create an instance of 
IceCreamStand, and call this method.
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

    # Class Restaurant End

class IceCreamStand(Restaurant):
    '''Store and display information about flavors of icecream'''
    
    def __init__(self, name, cusine, flavors):
        '''Initializing Attribute'''
        super().__init__(name, cusine)
        self.flavors = flavors


    def get_flavors(self):
        '''display all flavors'''
        print("List of Ice Cream Flavors:")
        for flavor in self.flavors:
            print("\t- "+ flavor.title())

    # Class IceCreamStand End


obj = IceCreamStand('the punjabi rosai', 'punjabi', ['vanilla', 'cookies and cream', 'chocolate', 'caramel'])
obj.describe_restaurant()
obj.get_flavors()