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

"""
NOTE:
- descriptive names
- only lowercase letters and underscores
- module name should follow this convention
- every function should have comment section,
  immediately after function defination
- no space in default value while assigning value (EX. name='pratik')
- if multiple parameter, start on new line and give two tab space 
    def function_name(
            parameter_0, parameter_1, parameter_2,
            parameter_3, parameter_4, parameter_5):
- give two new line gap between two function defination
- if import in program, it should be the first line except comment
"""
