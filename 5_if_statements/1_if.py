"""
> '==' is equality operator
> 'True' and 'False' is case sensitive
> Testing for equality is also case sensitive

"""

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("Displaying list of cars:")
for car in cars:
   if car == 'bmw':
      print(">", car.upper())
   else:
      print(">", car.title())

print("\nTesting for case sensitive:")
name = 'Python'
print(name)
print("name == 'python':", name == 'python')
print("name.lower() == 'python':", name.lower() == 'python')

print("\nChecking for inequality")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
   print("Hold the anchovies!")

print("\nLets do some numerical comparison:")
age = 21
if age == 21:
   print("You Passed!")
if age != 20:
   print("Well!, your age is not equal to 20")
if age < 20:
   print("Your age is less than 20")
if age <= 20:
   print("Your age is less than or equal to 20")
if age > 20:
   print("Your age is greater than 20")
if age >= 20:
   print("Your age is greater than or equal to 20")
if (age >= 18) and (age <= 30):
   print("Your age is between 18 and 30")   
if (age >= 18) or (age <= 10):
   print("Your age is greater than 18 or less than 10")

print("\nCheck value present in the list or not:")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:     # Check of availablity
   print("Added!!!") 
if 'pepperoni' not in requested_toppings:     # Check of not avaiable
   print("Sorry!, Topping not available...") 
