"""
Problem:
Write a function called city_country() that takes in the name of a city and its 
country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
"""

def city_country(city_name, country_name):
    """return formatted string"""
    formatted_name = city_name +", "+ country_name
    return formatted_name.title()

print("City-Country Pair")
name = city_country('mumbai', 'india')
print("1. "+ name)
name = city_country('tokyo', 'japan')
print("1. "+ name)
name = city_country('berlin', 'germany')
print("1. "+ name)