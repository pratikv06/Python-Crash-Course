# using in pass text case
def get_formatted_name(first, last):
    full_name = first +" "+ last
    return full_name.title()


# using in failed test case
def get_formatted_name2(first, middle, last):
    full_name = first +" "+ middle +" "+ last
    return full_name.title()


# using in responding to failed test case
def get_formatted_name3(first, last, middle=''):
    if middle:
        full_name = first +" "+ middle +" "+ last
    else:
        full_name = first +" "+ last
    return full_name.title()