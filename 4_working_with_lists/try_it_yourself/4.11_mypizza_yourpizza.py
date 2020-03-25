"""
Problem:
Start with your program from Exercise 4-1. Make a copy of the list of pizzas, 
and call it friend_pizzas.
Then, do the following:
> Add a new pizza to the original list.
> Add a different pizza to the list friend_pizzas.
> Prove that you have two separate lists. Print the message, My favorite pizzas 
  are:, and then use a for loop to print the first list. Print the message, My 
  friend’s favorite pizzas are:, and then use a for loop to print the second list.
  Make sure each new pizza is stored in the appropriate list.
"""
my_pizzas = ['Neapolitan', 'Salad', 'Kebab', 'Begal']
friend_pizzas = my_pizzas[:] # copied

my_pizzas.append('Baked Ziti')
friend_pizzas.append('Cheese')

print("My favorite pizzas are:")
for pizza in my_pizzas:
   print(">", pizza)

print("My friend's favorite pizza are:")
for pizza in friend_pizzas:
   print(">", pizza)