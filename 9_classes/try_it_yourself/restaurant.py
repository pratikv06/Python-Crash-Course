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