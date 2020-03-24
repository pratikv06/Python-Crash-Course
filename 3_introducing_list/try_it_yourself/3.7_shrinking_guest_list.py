"""
Problem:
You just found out that your new dinner table won’t arrive in time for the 
dinner, and you have space for only two guests .
> Start with your program from Exercise 3-6. Add a new line that prints a 
  message saying that you can invite only two people for dinner.
> Use pop() to remove guests from your list one at a time until only two names 
  remain in your list. Each time you pop a name from your list, print a message 
  to that person letting them know you’re sorry you can’t invite them to dinner.
> Print a message to each of the two people still on your list, letting them 
  know they’re still invited.
> Use del to remove the last two names from your list, so you have an empty 
  list. Print your list to make sure you actually have an empty list at the 
  end of your program.  
"""

guest = ['Gaurav', 'Shailesh', 'Pranjal', 'Ashutosh']
print("Guest list:")
print("Guest 1 :", guest[0])
print("Guest 2 :", guest[1])
print("Guest 3 :", guest[2])
print("Guest 4 :", guest[3])

guest.insert(0, 'Amit')
guest.insert(3, 'Naresh')
guest.append('Vishal')

print("Updated Guest list:")
print("Guest 1 :", guest[0])
print("Guest 2 :", guest[1])
print("Guest 3 :", guest[2])
print("Guest 4 :", guest[3])
print("Guest 5 :", guest[4])
print("Guest 6 :", guest[5])
print("Guest 7 :", guest[6])

print("Only 2 people can be invited:")
remove = guest.pop()
print("Sorry,", remove, "you are not invited.")

remove = guest.pop()
print("Sorry,", remove, "you are not invited.")

remove = guest.pop()
print("Sorry,", remove, "you are not invited.")

remove = guest.pop()
print("Sorry,", remove, "you are not invited.")

remove = guest.pop()
print("Sorry,", remove, "you are not invited.")

print("People who are invited:")
print("1.", guest[0])
print("2.", guest[1])

del guest[0]
del guest[0]
print("List of guest:", guest)