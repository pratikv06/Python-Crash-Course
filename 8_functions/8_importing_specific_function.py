# make use of from and import statement
# Example:
# from module_name import function_0, function_1, function_2

from module1 import make_pizza

# Here we can directly call the function
# Here we can't use `module_name.function_name` because module is not imported
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
NOTE:
- We can import all the function from the module
    > from module import *
- With this we don't have to write module name everytime we use function
- It's is not a best practice
"""