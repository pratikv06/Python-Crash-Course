"""
Problem:
An administrator is a special kind of user. Write a class called Admin that 
inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an 
attribute, privileges, that stores a list of strings like "can add post", "can 
delete post", "can ban user", and so on. Write a method called show_privileges() 
that lists the administrator’s set of privileges. Create an instance of Admin, 
and call your method.
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

class Admin(User):
    '''Admimistrator accss'''

    def __init__(self, firstname, lastname, privileges):
        '''Initializing attribute'''
        super().__init__(firstname, lastname)
        self.privileges = privileges


    def show_privileges(self):
        '''List of privileges'''
        print("List of privileges for this user is:")
        for privilege in self.privileges:
            print("\t-"+ privilege.title())

    # Class Admin End

obj = Admin('pratik', 'sharma', ['can add post', 'can add user', 'can delete user',
             'can delete post', 'can ban user', 'can add privileges to user'])
obj.describe_user()
obj.show_privileges()
