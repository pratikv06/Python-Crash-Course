import json

filename = 'file4_number.json'

with open(filename, 'r') as file:
    numbers = json.load(file)

print(numbers)

# Note:
# load():
# take file object