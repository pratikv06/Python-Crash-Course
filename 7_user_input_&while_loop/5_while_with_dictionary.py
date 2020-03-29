print(">> Filling a dictionary with user input")
responses = {}
active_polling = True
while active_polling:
    # taking input
    name = input("What is your name? ")
    book = input("Which book you want to read? ")
    # Storing in dictionary
    responses[name] = book
    # Continue Polling?
    repeat = input("Would you like to take another person response (y/n)? ")
    if repeat.lower() == 'n':
        active_polling = False
print("--- Polling result ---")
for name, book in responses.items():
    print(name.title() +" want to read "+ book.title() +".")
