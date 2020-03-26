print(">> Example of If-else statement")
age = 17
if age >= 18:
   print("You are old enough to vote!")
   print("have you registered to vote yet?")
else:
   print("Sorry, you are too young to vote...")
   print("Please register to vote as soon as you turn 18!")

print("\n>> Example of If-elif-else statement")
age = 12
if age < 4:
   print("Your admission cost is $0.")
elif age < 18:
   print("Your admission cost is $5.")
else:
   print("Your admission cost is $10.")

print("\n>> We can also make use of variable to store price and \n>> print at the end of the if-elif-else block")
age = 69
if age < 4:
   price = 0
elif age < 18:
   price = 5
elif age < 65:
   price = 10
else:
   price = 5 # $5 discount to senior citizen (above 65)
print("Your admission cost is $"+ str(price) +".")

# we can replace the else block with elif block for more surety of the output