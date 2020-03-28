print("Print number from 1 to 5")
count = 1
while count <= 5:
    print(count, end=", ")
    count += 1

print("\nLets the users to choose when to exit")
print("To exit enter quit, otherwise same text will be printed")
message = ""
while message.lower() != 'quit':
    message = input("Enter your string: ")
    if message.lower() != 'quit':
        print("> "+ message)

print("\nLets change the above code using flag")
print("To exit enter quit, otherwise same text will be printed")
active = True
while active:
    message = input("Enter your string: ")
    if message.lower() == 'quit':
        active = False
    else:
        print("> "+ message)