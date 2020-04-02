# This module conatin function make_pizza()

def make_pizza(size, *topping):
    """Summarize the pizza we are about to make."""
    print("Make a "+ str(size) +"-inch pizza with the following topping -")
    for top in topping:
        print("\t- "+ top)