"""
Problem:
Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user 
profile. Make a method called describe_user() that prints a summary of the 
user’s information. Make another method called greet_user() that prints a 
personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user.
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

user_obj1 = User('pratik', 'sharma')
user_obj2 = User('nilesh', 'yadav')

print("Object 1:")
user_obj1.describe_user()
user_obj1.greet_user()

print("\nObject 2:")
user_obj2.describe_user()
user_obj2.greet_user()