'''Note:
Refactoring:
- improving the code by breaking it up into series of function
- Makes: code cleaner, easier to understand, and easier to extend '''

import json

def get_stored_username():
    '''Get stored username if available'''
    filename = 'file5_username.json'
    try:
        with open(filename, 'r') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''Prompt for a new username'''
    filename = 'file5_username.json'
    username = input("What is your Name? \n>>> ")
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    '''Great the user by name'''
    username = get_stored_username()
    if username:        
        print(f"Welcome Back, {username}!")
    else:
        username = get_new_username()
        print("We'll remember you when you came back, "+ username +"!")

greet_user()