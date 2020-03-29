"""
Problem:
Make a dictionary called cities. Use the names of three cities as keys in your 
dictionary. Create a dictionary of information about each city and include the 
country that the city is in, its approximate population, and one fact about that 
city. The keys for each city’s dictionary should be something like country, 
population, and fact. Print the name of each city and all of the information
you have stored about it.
"""
cities = {
    'mumbai': {
        'country': 'india',
        'state': 'maharashtra',
        'area': '603.4 km',
        'population': '1.84 crores',
        'language': 'marathi',
    },
    'pune': {
        'country': 'india',
        'state': 'maharashtra',
        'area': '331.3 km',
        'population': '31.2 lakhs',
        'language': 'marathi',
    },
    'banglore': {
        'country': 'india',
        'state': 'karnataka',
        'area': '709 km',
        'population': '84.3 lakhs',
        'language': 'kannada',
    },
    'new delhi': {
        'country': 'india',
        'state': 'delhi',
        'area': '1484 km',
        'population': '1.9 crores',
        'language': 'hindi',
    },
}

for city, cityinfo in cities.items():
    print("City : "+ city.title())
    for key, info in cityinfo.items():
        print("\t"+ key.title() +" : "+ info.title())