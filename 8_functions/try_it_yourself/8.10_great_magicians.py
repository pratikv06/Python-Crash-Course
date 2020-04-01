"""
Problem:
Start with a copy of your program from Exercise 8-9 . Write a function called 
make_great() that modifies the list of magicians by adding the phrase the Great
to each magician’s name. Call show_magicians() to see that the list has actually 
been modified.
"""
def make_great(magicians_list):
    """Add great to the name"""
    for i in range(len(magicians_list)):
        magicians_list[i] = "great " + magicians_list[i]

def show_magicians(magicians_list):
    """displaying all the magician in the list"""
    for person in magicians_list:
        print("\t- "+ person.title())

magicians_list = ['pratik', 'vishal', 'purvesh']
make_great(magicians_list)
show_magicians(magicians_list)