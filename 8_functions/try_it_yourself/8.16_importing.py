"""
Problem:
Using a program you wrote that has one function in it, store that function in a 
separate file. Import the function into your main program file, and call the 
function using each of these approaches:
    import module_name
    from module_name import function_name
    from module_name import function_name as fn
    import module_name as mn
    from module_name import *
"""

import print_model
from print_model import display_model
from print_model import display_model as dm 
import print_model as pm
from print_model import *
model_list = ['ferrari', 'honda', 'maruti', 'hero']

print(">> Using module name :")
print_model.display_model(model_list)

print("\n>> Using function name :")
display_model(model_list)

print("\n>> Using function alias name :")
dm(model_list)

print("\n>> Using module alias name :")
pm.display_model(model_list)

print("\n>> Using function name when all function are imported :")
display_model(model_list)
