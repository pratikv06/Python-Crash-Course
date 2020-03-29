# def - use to define function in python
# after def is the name of the function 
# finally defination end with colon(:)
# any indented line that follow def fun_name(): make up the body of function

# Definiting a function
def greet_user():
    """Display a simple freeting."""
    print("Hello.")

# calling a function
greet_user()

#Function accept parameter
def greet_user2(name):  # parameter
    """Display a Simple message"""
    print("Hello, "+ name.title() +"!")

greet_user2("pratik") # argument