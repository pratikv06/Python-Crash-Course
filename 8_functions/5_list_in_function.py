print(">> Passing a list to the function")
def greet_user(names):
    """Print a simple greeting to all the user"""
    for name in names:
        msg = "Hello, "+ name.title() +"!"
        print(msg)
usernames = ['pratik', 'nilesh', 'yash']
greet_user(usernames)

print("\n>> Modifying a list in function")
# Note that when you pass a list to a function,
# the function can modify the list 
def print_model(unprinted_designs, completed_models):
    """Move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Model: "+ current_design.title())
        completed_models.append(current_design)

def show_completed_model(completed_models):
    """Display all the completed model"""
    print("Following model have been printed:")
    for model in completed_models:
        print("\t- "+ model.title())
    
unprinted_designs = ['iphone case', 'robot pendent', 'dodechedron']
completed_models = []
print_model(unprinted_designs, completed_models)
show_completed_model(completed_models)

# Note:
# If you want to make a copy of the list so that any changes made in the function 
# is not reflected on the list.
# Use the `slice notation` to send copy of the list to the function.