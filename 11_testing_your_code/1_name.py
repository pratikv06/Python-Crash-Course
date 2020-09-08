from module1_name_formatting import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("Enter First Name: ")
    if first.lower() == 'q':
        break

    last = input("Enter Last Name: ")
    if last.lower() == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly foramtted Name: "+ formatted_name)