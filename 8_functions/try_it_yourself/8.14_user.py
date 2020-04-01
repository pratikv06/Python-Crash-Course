"""
Problem:
Write a function that stores information about a car in a dictionary. The 
function should always receive a manufacturer and a model name. It should then
accept an arbitrary number of keyword arguments. Call the function with the 
required information and two other name-value pairs, such as a color or an
optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""
def make_car(manufacturer, car_model, **car_infos):
    """Create a dictionary of car info"""
    car_desc = {
        'manufacturer': manufacturer,
        'car_model': car_model
    }
    for key, value in car_infos.items():
        car_desc[key] = value
    return car_desc

car_detail = make_car('hero', 'RX125', color= 'red', air_bag= 'yes')
print("Car Deatil :")
print(car_detail)
car_detail = make_car('bajaj', 'dezir', color= 'grey', air_bag= 'yes', cng= 'no')
print("Car Deatil :")
print(car_detail)