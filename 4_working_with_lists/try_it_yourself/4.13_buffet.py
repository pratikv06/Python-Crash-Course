"""
Problem:
A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
> Use a for loop to print each food the restaurant offers.
> Try to modify one of the items, and make sure that Python rejects the
change.
> The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
"""

foods = ('Alu Gobhi', 'Barfi', 'Carrot Halwa', 'Chat Papri', 'Chicken 65')
print("Food List:")
for food in foods:
   print(">", food)

# This will print error 
# foods[0] = 'Alu Matart'

print("Updated Food List:")
foods = ('Alu Matar', 'Barfi', 'Chana Dal', 'Chat Papri', 'Chicken 65')
for food in foods:
   print(">", food)