# Argument can be passed in two ways
# 1. positional Argument - order of argument passed matter
# 2. Keyword Argument

print(">> Example of Positional Argument")

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a "+ animal_type +".")
    print("My "+ animal_type +"'s name is "+ pet_name.title())
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')   # Calling a function second time
describe_pet('harry', 'hamster')    # Order matters in positional argument

print("\n>> Example of Keyword Argument")
# use the exact names of the parameters in the function’s definition
describe_pet(animal_type='hamster', pet_name='harry') 
describe_pet(pet_name='harry', animal_type='hamster')


print("\n>> Example of default value")

def describe_pet2(pet_name,animal_type='dog'):
    """Display info about a pet"""
    print("\nI have a "+ animal_type +".")
    print("My "+ animal_type +"'s name is "+ pet_name.title())
# animal type is not passed, pet_name is treated as positional argument that why default is at the extreme right 
describe_pet2('willie')
describe_pet2(pet_name='harry', animal_type='hamster') #animal type is passed