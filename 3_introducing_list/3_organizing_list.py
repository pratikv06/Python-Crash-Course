# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original List:", cars)
cars.sort() # change the order of the list to store them alphabetically
print("Sorted list:", cars)

# sort this list in reverse alphabetical order by passing the argument 
# reverse=True to the sort() method
cars.sort(reverse=True)
print("Reverse Sorted List:", cars)

# Sorting a List Temporarily with the sorted() Function
# To maintain the original order of a list but present it in a sorted order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nOriginal list:", cars)
print("Sorted list:", sorted(cars))
print("Reversed sorted list:", sorted(cars, reverse=True))
print("Original list again:", cars)

# Printing a List in Reverse Order
# reverse() doesn’t sort backward alphabetically; 
# it simply reverses the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original List:", cars)
cars.reverse()
print("Reversed List:", cars)

# Finding the Length of a List
print("length of the list cars:", len(cars) )