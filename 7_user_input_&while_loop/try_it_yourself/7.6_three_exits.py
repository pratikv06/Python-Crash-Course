"""
Problem:
Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of 
the following at least once:
> Use a conditional test in the while statement to stop the loop.
> Use an active variable to control how long the loop runs.
> Use a break statement to exit the loop when the user enters a 'quit' value.
"""
print(">> Conditonal Test:")
while True:
    age = int(input("Age of the person : "))
    if age > 20:
        break
    elif age < 3:
        print("Ticket is free.")
    elif age < 13:
        print("Ticket fair is $10.")
    elif age > 12:
        print("Ticket fair is $15.")


print("\n>> Active Variable")
count = 0
while count < 3:
    count += 1
    age = int(input("Age of the person : "))
    if age < 3:
        print("Ticket is free.")
    elif age < 13:
        print("Ticket fair is $10.")
    elif age > 12:
        print("Ticket fair is $15.")

print("\n>> Break statement when enter quit")
while True:
    age = input("Age of the person : ")
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Ticket is free.")
    elif int(age) < 13:
        print("Ticket fair is $10.")
    elif int(age) > 12:
        print("Ticket fair is $15.")
