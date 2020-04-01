# print(">> Arbitrary Number of argument in the function")
# def make_pizza(*topping):
#     """Printing all the pizza topping"""
#     print(type(topping))
#     print(topping)

# make_pizza('pepperoni')
# make_pizza('extra cheese', 'mushrooms', 'pepperoni', 'green peppers')


# print("\n>> Mixing postional and arbitrary arguments")
# # arbitrary argument must be placed last in the function defination
# def make_pizza2(size, *topping):  # * for tuple
#     """Printing all the pizza topping"""
#     print("Size of the pizza is", size, "and topping are:")
#     print(topping)
# make_pizza2(12, 'pepperoni')
# make_pizza2(16, 'extra cheese', 'mushrooms', 'pepperoni', 'green peppers')

print("\n>> Using arbitrary keyword argument")
def build_profile(first, last, **user_info): # ** for dictionary
    """Build dictionary containing user information"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('pratik', 'vishwakarma',
                            location= 'pune', job= 'system programmer', 
                            experience= '5 years')
print(user_profile)