"""
Problem:
Use a dictionary to store information about a person you know. Store their 
first name, last name, age, and the city in which they live. You should have 
keys such as first_name, last_name, age, and city. Print each piece of 
information stored in your dictionary.
"""

person = {
    'first_name': 'Nilesh',
    'last_name': 'Pal',
    'age': 24,
    'city': 'Mumbai',
}

for key in person:
    print(key, ">", person[key])