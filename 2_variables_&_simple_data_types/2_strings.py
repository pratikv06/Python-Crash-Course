# string is simply a series of characters
# Anything inside quotes is considered a string in Python
# you can use single or double quotes around your strings

str = 'I told my friend, "Python is my favorite language!"'
print("String 1 : ", str)

str = "The language 'Python' is named after Monty Python, not the snake."
print("String 2 : ", str)

str = "One of Python's strengths is its diverse and supportive community."
print("String 3 : ", str)

print("\n*** Function of String ***")

print("1. Changing case in a string with method")
name = "aDa LoVeLaCe"
print("\tOriginal Value : ", name)
print("\ttitle method   : ", name.title())
print("\tlower method   : ", name.lower())
print("\tupper method   : ", name.upper())
# Method: an action that Python can perform on a piece of data
# dot (.): tells Python to make the title() method act on the variable name
# title(): displays each word in titlecase, where each word begins with a capital letter

print("\n2. Combining or Concatenating Strings")
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "\tHello, " + full_name.title() + "!"
print(message)

print("\n3. Adding Whitespace to Strings with Tabs or Newlines")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# \t: add tab to your text
# \n: enter new line

print("\n4. Stripping Whitespace")
favorite_language = ' python '
print("\tSpace removed from right    : '"+ favorite_language.rstrip() +"'")
print("\tSpace removed from left     : '"+ favorite_language.lstrip() +"'")
print("\tSpace removed from both end : '"+ favorite_language.strip() +"'")
