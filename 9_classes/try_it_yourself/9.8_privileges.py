"""
Problem:
Write a separate Privileges class. The class should have one attribute, 
privileges, that stores a list of strings as described in Exercise 9-7. Move 
the show_privileges() method to this class. Make a Privileges instance as an 
attribute in the Admin class. Create a new instance of Admin and use your method 
to show its privileges.
"""
class User():
    """Store User Information"""
    def __init__(self, firstname, lastname):
        """Initializing attribute"""
        self.first_name = firstname
        self.last_name = lastname
        self.full_name = firstname +" "+ lastname

    
    def describe_user(self):
        '''Display user info'''
        print("** USER INFO **")
        print("User first name is - "+ self.first_name.title())
        print("User last name is - "+ self.last_name.title())
        print("User full name is - "+ self.full_name.title())    


    def greet_user(self):
        '''Printing greeting message for user'''
        print(">> Welcome, "+ self.full_name.title() +" to world of python!")

    # End Class

class Privilege():
    '''Class to store Privilege of user'''
    def __init__(self, privileges):
        self.privileges = privileges


    def show_privileges(self):
        '''List of privileges'''
        print("List of privileges for this user is:")
        for privilege in self.privileges:
            print("\t-"+ privilege.title())

    # Class Privilege End

class Admin(User):
    '''Admimistrator accss'''
    def __init__(self, firstname, lastname, privileges):
        '''Initializing attribute'''
        super().__init__(firstname, lastname)
        self.privilege = Privilege(privileges)

    # Class Admin End

obj = Admin('pratik', 'sharma', ['can add post', 'can add user', 'can delete user',
             'can delete post', 'can ban user', 'can add privileges to user'])
obj.describe_user()
obj.privilege.show_privileges()
