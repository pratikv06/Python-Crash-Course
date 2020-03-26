"""
Problem:
Add an if test to hello_admin.py to make sure the list of users is not empty.
> If the list is empty, print the message We need to find some users!
> Remove all of the usernames from your list, and make sure the correct message 
  is printed.
"""


# usernames = ['Pratik', 'Vishal', 'Amit', 'Admin', 'Yash']
usernames = []
if usernames:
   for name in usernames:
      if name == 'Admin':
         print("Hello "+ name +", would you like to see a status report?")
      else:
         print("Hello "+ name +", Thank You for logging in again.")
else:
   print("No user info available..")