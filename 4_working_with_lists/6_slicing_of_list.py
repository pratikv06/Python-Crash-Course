# To make a slice, you specify the ix of first and last element you want to work with.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Player from index 0 to 3:",players[0:3])
# this will print value at index 0, 1, and 2 
# not the index 3, same as range function
print("Player from index 1 to 4", players[1:4])
print("Player from index _ to 4", players[:4]) # Start slicing from the start of the list
print("Player from index 2 to _", players[2:]) # End Slicing till end of the list
print("Only last 3 Player", players[-3:])

print("Looping through first three player in the list")
for player in players[:3]:
   print(player.title())

print("\n\nLet make a copy of list:")
my_foods = ['pizza', 'cake', 'burger']
friend_foods = my_foods[:]
print("My favorite food:", my_foods)
print("My friends favorite food:", friend_foods)
print(">> To make sure that these list are two seperate list. <<\n>> Add new food in each list. <<")
my_foods.append('icecream')
friend_foods.append('falafel')
print("My favorite food:", my_foods)
print("My friends favorite food:", friend_foods)

print("\n>> Now make a copy without slicing the list:")
new_food = ['pizza', 'cake', 'burger']
copy_food = new_food
print("new food list", new_food)
print("copied food list", copy_food)
print(">> Now append a value in new food list")
new_food.append('ice cream')
print("new food list", new_food)
print("copied food list", copy_food)
# This means both the list are pointing to same memory loaction