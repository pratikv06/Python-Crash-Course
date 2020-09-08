import json

username = input("What is your Name? \n>>> ")

filename = 'file5_username.json'

with open(filename, 'w') as file:
    json.dump(username, file)
    print("We'll remember you when you came back, "+ username +"!")