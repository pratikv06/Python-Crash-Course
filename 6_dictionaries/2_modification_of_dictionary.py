print("Initialize an empty dictionary and add value to it.")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 5
print("Value of Dictionary:", alien_0)

print("\nChanging the color of alien to red")
alien_0['color'] = 'red'
print("Value of Dictionary:", alien_0)

print("\nLet remove the point key from the dictionary")
del alien_0['point']    # Key-value pair ramoved permanently
print("Value of Dictionary:", alien_0) 
