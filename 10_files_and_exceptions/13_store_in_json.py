import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

filename = 'file4_number.json'

with open(filename, 'w') as file:
    json.dump(numbers, file)

# Note
# dump() - to store data in json
# take two argument:
# 1. data to store and 2. file object