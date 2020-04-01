"""
Problem:
Write a function that accepts a list of items a person wants on a sandwich. The 
function should have one parameter that collects as many items as the function 
call provides, and it should print a summary of the sandwich that is being
ordered. Call the function three times, using a different number of arguments
each time.
"""
def make_sandwich(*items):
    """Summary of sandwitch items"""
    print("Here the list of items to add in sandwitch:")
    for item in items:
        print("\t- "+ item.title())
make_sandwich()
make_sandwich('extra cheese')
make_sandwich('cheese', 'onion')
make_sandwich('tomato', 'cheese', 'onion', 'paneer')