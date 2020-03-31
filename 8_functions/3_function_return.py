print(">> Define a function that return a value")

def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    full_name = first_name +" "+ last_name
    return full_name.title()

person = get_formatted_name('nilesh', 'yadav')
print(person)

print("\n>> making a argument optional")

def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    full_name = first_name +" "+ middle_name +" "+ last_name
    return full_name.title()
person = get_formatted_name2('nilesh', 'yadav', 'suresh')
print(person)
person = get_formatted_name2('nlesh', 'yadav')
print(person)

print("\n>> Returning dictionary from a function")
def build_person(first_name, last_name, age=''):
    """Return a dictionary of person information"""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person
detail = build_person('pratik', 'vishwakarma', 12)
print(detail)