'''
Problem:
Using your latest Restaurant class, store it in a module. Make a separate file
that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s
methods  to show that the import statement is working properly.
'''

import restaurant

restaurant_obj = restaurant.Restaurant('the punjabi rosai', 'punjabi')
restaurant_obj.describe_restaurant()
restaurant_obj.get_served_number()