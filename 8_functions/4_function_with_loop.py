def get_formatted_name(first_name, last_name):
    """Return Fullname, neatly formatted"""
    fullname = first_name +" "+ last_name
    return fullname.title()

while True:
    print("Enter 'q' anytime to quit")
    print("Tell me your name: ")
    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)