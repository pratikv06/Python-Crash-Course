# `as` keyword is used to create alias
# when alias is create we can't use the ogrinal name of the module or function
# Example
# from module_name import function_name as fn

from module1 import make_pizza as mp
# make_pizza will give error
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')