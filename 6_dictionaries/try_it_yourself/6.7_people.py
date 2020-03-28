"""
Problem:
Start with the program you wrote for Exercise 6-1. Make two new dictionaries 
representing different people, and store all three dictionaries in a list 
called people. Loop through your list of people. As you loop through the list, 
print everything you know about each person.
"""
person_1 = {
    'first_name': 'nilesh',
    'last_name': 'yadav',
    'age': 21,
    'city': 'Pune',
}
person_2 = {
    'first_name': 'jay',
    'last_name': 'singh',
    'age': 20,
    'city': 'Mumbai',
}
person_3 = {
    'first_name': 'ratnesh',
    'last_name': 'dubey',
    'age': 24,
    'city': 'ranchi',
}

people = [person_1, person_2, person_3]
for person in people:
    print(person)