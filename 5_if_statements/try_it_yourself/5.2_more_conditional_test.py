"""
Problem:
You don’t have to limit the number of tests you create to 10. If you want to 
try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
> Tests for equality and inequality with strings
> Tests using the lower() function
> Numerical tests involving equality and inequality, greater than and less than, 
  greater than or equal to, and less than or equal to
> Test whether an item is in a list
> Test whether an item is not in a list
"""

str = 'Python'
print("** str = ", str, " **")
print("Is str == 'Python' > ", end="")
print(str == 'Python')
print("Is str != 'python' > ", end="")
print(str != 'python')

print("Is str.lower() == 'python' > ", end="")
print(str.lower() == 'python')

num = 22
print("\n** num = ", num, " **")
print("Is num == 22 >", end=" ")
print(num == 22)
print("Is num != 22 >", end=" ")
print(num != 22)
print("Is num > 22 >", end=" ")
print(num > 22)
print("Is num >= 22 >", end=" ")
print(num >= 22)
print("Is num < 22 >", end=" ")
print(num < 22)
print("Is num <= 22 >", end=" ")
print(num <= 22)

items = ['Monitor', 'Keyboard', 'Mouse', 'Speaker', 'PC', 'Headphone', 'Internet', 'WiFi']
print("\n** List = ", items, " **")
if 'Monitor' in items:
  print("Yes, Monitor is in the list.")
if 'Trackpad' not in items:
     print("We have to add Trackpad in the list...")
