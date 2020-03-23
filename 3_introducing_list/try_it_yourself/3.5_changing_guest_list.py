"""
Problem:
You just heard that one of your guests can’t make the dinner, so you need to 
send out a new set of invitations. You’ll have to think of someone else to invite.
> Start with your program from Exercise 3-4. Add a print statement at the end of
  your program stating the name of the guest who can’t make it.
> Modify your list, replacing the name of the guest who can’t make it with the 
  name of the new person you are inviting.
> Print a second set of invitation messages, one for each person who is still
  in your list.
"""

guest = ['Gaurav', 'Shailesh', 'Pranjal', 'Ashutosh']
print("Guest list:")
print("Guest 1 :", guest[0])
print("Guest 2 :", guest[1])
print("Guest 3 :", guest[2])
print("Guest 4 :", guest[3])

print("Guest Who can't make it: Shailesh and Pranjal")
# Removing Guest
guest.remove('Shailesh')
guest.remove('Pranjal')
# Adding New guest
guest.append('Amit')
guest.append('Naresh')

print("New Guest list:")
print("Guest 1 :", guest[0])
print("Guest 2 :", guest[1])
print("Guest 3 :", guest[2])
print("Guest 4 :", guest[3])