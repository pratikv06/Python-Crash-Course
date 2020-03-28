print(">> Using break to exit the while loop")
print("To exit, type `quit`")
while True:
    message = input("Enter your message: ")
    if message.lower() == 'quit':
        break
    else:
        print(">", message)

print("\n>> use of continue")
print("Let's Print Even number from 1 - 10")
count = 0
while count <= 10:
    count += 1
    if count%2 != 0:
        continue
    print(count, end=", ")