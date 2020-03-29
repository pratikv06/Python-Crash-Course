"""
Problem:
Write a program that polls users about their dream vacation. Write a prompt 
similar to If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll.
"""

responses = {}
active_polling = True
while active_polling:
    # taking input
    name = input("What is your name? ")
    place = input("Which place you like to visit in world? ")
    # Storing in dictionary
    responses[name] = place
    # Continue Polling?
    repeat = input("Would you like to take another person response (y/n)? ")
    if repeat.lower() == 'n':
        active_polling = False
print("--- Polling result ---")
for name, place in responses.items():
    print(name.title() +" want to visit "+ place.title() +".")