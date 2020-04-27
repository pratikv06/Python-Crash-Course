"""
Problem:
Start with your work from Exercise 9-8. Store the classes User, Privileges, and 
Admin in one module. Create a separate file, make an Admin instance, and call
show_privileges() to show that everything is working correctly.

Note:
Module file name -
1. users
"""

import users

myobj = users.Admin('pratik', 'sharma', ['can add post', 'can add user', 'can delete user',
             'can delete post', 'can ban user', 'can add privileges to user'])
myobj.privilege.show_privileges()
