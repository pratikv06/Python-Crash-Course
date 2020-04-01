"""
Problem:
Make a list of magician’s names. Pass the list to a function called 
show_magicians(), which prints the name of each magician in the list.
"""

def show_magicians(magician_list):
    """Display magicians name"""
    for person in magician_list:
        print("Mr. "+ person.title() +"!")

magician_list = ['pratik', 'vishal', 'purvesh']
show_magicians(magician_list)