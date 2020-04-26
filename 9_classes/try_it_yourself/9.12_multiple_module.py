'''
Problem:
Store the User class in one module, and store the Privileges and Admin classes 
in a separate module. In a separate file, create an Admin instance and call 
show_privileges() to show that everything is still working correctly.

Note: 
Module file name -
1. adminclass
2. privilege
'''

import adminclass

myobj = adminclass.Admin('pratik', 'sharma', ['can add post', 'can add user', 'can delete user',
             'can delete post', 'can ban user', 'can add privileges to user'])
myobj.privilege.show_privileges()
