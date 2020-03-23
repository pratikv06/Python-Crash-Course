# Initializing list
motorcycles = ['honda', 'yamaha', 'suzuki', 'bajaj', 'KTM', 'Royal Enfield']
print("List Values:", motorcycles)

# adding new value - using append() method
# This will add element at the end of the list
motorcycles.append('ducati')
print("Updated List:", motorcycles)

# let create a new list and add element using append() method
vehicles = [] # Initializing empty list
vehicles.append('honda')
vehicles.append('yamaha')
vehicles.append('suzuki') 
print("New List:", vehicles)

# adding new value - using insert() method
# This will add element at the given index
# and shift other by 1 position to right
motorcycles.insert(0, 'hero')
print("Insert at index 0:", motorcycles)

# removing an Item Using the del Statement
del motorcycles[1]
print("Deleting Element at position 2:",motorcycles)

# removing an Item Using the pop() Method
# The pop() method removes the last item in a list, 
# but it lets you work with that item after removing it
popped_motorcycle = motorcycles.pop()
print("After removing last element from the list:",motorcycles)
print("Last removed element:",popped_motorcycle)

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# removing an Item by Value
# when  we dont know the position of the element in the list
# The remove() method deletes only the first occurrence of the value you specify
motorcycles.remove('bajaj')
print("After removing bajaj from list:",motorcycles)