"""
- What is list?
> A list is a collection of items in a particular order
> You can make a list that includes the letters of the alphabet, the digits 
  from 0–9, or the names of all the people in your family

- Square brackets ([]) indicate a list
- individual elements in the list are separated by commas
- Index position start at 0 (Zero)
- last Element can be pointed using -1
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("Printing List:\n", bicycles)
print("Element at index 0 :", bicycles[0].title())
print("Element at position 3 :", bicycles[2])
print("Element at last index :", bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)