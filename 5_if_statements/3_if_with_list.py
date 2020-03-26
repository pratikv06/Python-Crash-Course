print(">> Let assume we don't have green peppers in stock")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
   if requested_topping == 'green peppers':
      print("Sorry, we are out of green peppers right now.")
   else:
      print("Adding " + requested_topping + ".")
print("-- Finished making your pizza!")

print("\n\n>> Before we start working with list, \n>> We have to check if the list is not empty!")
print(">> If empty, display appropriate message.")
requested_toppings = []
if requested_toppings:
   for requested_topping in requested_toppings:
      print("Adding " + requested_topping + ".")
   print("\nFinished making your pizza!")
else:
   print("Are you sure you want a plain pizza?")

print("\n\n>>This time we compare the requested topping value with the avaiable topping")
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
   if requested_topping in available_toppings:
      print("Adding " + requested_topping + ".")
   else:
      print("Sorry, we don't have " + requested_topping + ".")       
print("-- Finished making your pizza!")