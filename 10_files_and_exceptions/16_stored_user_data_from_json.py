# Assuming the json file is not present
import json

filename = 'file5_username.json'
with open(filename, 'r') as file:
    username = json.load(file)
print(f"Welcome Back, {username}!")