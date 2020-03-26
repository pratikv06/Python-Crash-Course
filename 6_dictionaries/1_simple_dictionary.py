"""
- Collection of key-value pairs
- {} indicate dictionary
- Each key is connected to a value
- Using key we can access the associated value to that key
- key can be anything - a number, a string, a list, or even another dictionary
- Each key and value is seperated by colon (:)
- Each key-value pair is seperated by comma (,)
"""

alien_0 = {
    'color': 'green',
    'points': 5
}
print("Directly using dictionary name:", alien_0)
print("\nAccessing value using key")
print(">", alien_0["color"])
print(">", alien_0["points"])

print("\nAdding coordinate of the alien in the dictionary")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("Updated value:", alien_0)