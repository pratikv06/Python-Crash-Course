"""
Problem:
You just found a bigger dinner table, so now more space is available. Think of 
three more guests to invite to dinner.
> Start with your program from Exercise 3-4 or Exercise 3-5. Add a print 
  statement to the end of your program informing people that you found a bigger
  dinner table.
> Use insert() to add one new guest to the beginning of your list.
> Use insert() to add one new guest to the middle of your list.
> Use append() to add one new guest to the end of your list.
> Print a new set of invitation messages, one for each person in your list.
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