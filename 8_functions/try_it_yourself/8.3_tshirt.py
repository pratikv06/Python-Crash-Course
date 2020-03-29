"""
Problem:
Write a function called make_shirt() that accepts a size and the text of a 
message that should be printed on the shirt. The function should print a 
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

def make_shirt(shirt_size, shirt_text):
    """Display Shirt Detail"""
    print("Size of the shirt is "+ shirt_size +"\nThe message printed on it is "+ shirt_text)
make_shirt("medium", "Python is awesome")
make_shirt(shirt_text="let code", shirt_size="large")