"""
Problem:
Write a loop that prompts the user to enter a series of pizza toppings until 
they enter a 'quit' value. As they enter each topping, print a message saying 
you’ll add that topping to their pizza.
"""
topping = ''
while topping != 'quit':
    topping = input("Enter pizza topping : ")
    if topping != 'quit':
        print("> "+ topping.title() +" will be added to pizza topping.")
