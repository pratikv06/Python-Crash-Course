"""
Problem:
Modify the make_shirt() function so that shirts are large by default with a 
message that reads I love Python. Make a large shirt and a medium shirt with 
the default message, and a shirt of any size with a different message.
"""
def make_shirt(shirt_size="large", shirt_text="I love Python"):
    """Display Shirt Detail"""
    print("Size of the shirt is "+ shirt_size +"\nThe message printed on it is "+ shirt_text)
make_shirt()
make_shirt("medium", "Python is awesome")