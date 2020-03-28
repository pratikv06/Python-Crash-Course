"""
Problem:
Make a dictionary called favorite_places. Think of three names to use as keys 
in the dictionary, and store one to three favorite places for each person. To 
make this exercise a bit more interesting, ask some friends to name a few of 
their favorite places. Loop through the dictionary, and print each person’s 
name and their favorite places.
"""
fav_places = {
    'ratnesh': 'toyko',
    'prakash': 'delhi',
    'raj': 'colosseum',
}

for name, place in fav_places.items():
    print(name.title() +"'s favorite place is "+ place.title())