"""
Problem:
Working with one of the programs from Exercises 3-4 through 3-7, use len() to 
print a message indicating the number of people you are inviting to dinner.
"""
# 3.4
guest = ['Gaurav', 'Shailesh', 'Pranjal', 'Ashutosh']
print("Guest in 3.4:", len(guest))
# 3.5
guest.remove('Shailesh')
guest.remove('Pranjal')
guest.append('Amit')
guest.append('Naresh')
print("Guest in 3.5:", len(guest))
# 3.6
guest.insert(0, 'Shailesh')
guest.insert(3, 'Pranjal')
guest.append('Vishal')
print("Guest in 3.6:", len(guest))
# 3.7
remove = guest.pop()
remove = guest.pop()
remove = guest.pop()
remove = guest.pop()
remove = guest.pop()
del guest[0]
del guest[0]
print("Guest in 3.7:", len(guest))