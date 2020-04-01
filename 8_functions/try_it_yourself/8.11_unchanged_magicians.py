"""
Problem:
Start with your work from Exercise 8-10. Call the function make_great() with 
a copy of the list of magicians’ names. Because the original list will be 
unchanged, return the new list and store it in a separate list. Call 
show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
"""

def make_great(magicians_list):
    """Add great to the name"""
    for i in range(len(magicians_list)):
        magicians_list[i] = "great " + magicians_list[i]
    return magicians_list

def show_magicians(magicians_list):
    """displaying all the magician in the list"""
    for person in magicians_list:
        print("\t- "+ person.title())

magicians_list = ['pratik', 'vishal', 'purvesh']
updated_magicians_list = make_great(magicians_list[:])
print("Original List:")
show_magicians(magicians_list)
print("Updated List:")
show_magicians(updated_magicians_list)