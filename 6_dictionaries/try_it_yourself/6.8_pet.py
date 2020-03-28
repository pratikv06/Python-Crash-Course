"""
Problem:
Make several dictionaries, where the name of each dictionary is the name of a 
pet. In each dictionary, include the kind of animal and the owner’s name. Store 
these dictionaries in a list called pets. Next, loop through your list and as 
you do print everything you know about each pet.
"""
ricky =  {
    'animal': 'dog',
    'owner': 'nilesh'
}
monty = {
    'animal': 'hamster',
    'owner': 'shaker'
}
mike = {
    'animal': 'cat',
    'ower': 'heem'
}
pets = [ricky, monty, mike]
for pet in pets:
    print(pet)