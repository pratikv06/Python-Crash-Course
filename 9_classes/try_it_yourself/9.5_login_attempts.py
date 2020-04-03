"""
Problem:
Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of 
login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts() several 
times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0.
"""

class User():
    """Store User Information"""

    def __init__(self, firstname, lastname):
        """Initializing attribute"""
        self.first_name = firstname
        self.last_name = lastname
        self.full_name = firstname +" "+ lastname
        self.login_attempts = 0

    
    def describe_user(self):
        '''Display user info'''
        print("** USER INFO **")
        print("User fssrt name is - "+ self.first_name.title())
        print("User last name is - "+ self.last_name.title())
        print("User full name is - "+ self.full_name.title())    


    def get_login_attempt(self):
        '''display number of login attempts'''
        print("Total login attempts : "+ str(self.login_attempts))

    
    def increment_login_attempts(self):
        '''increasing the value by one'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        '''Resting the login attempts to 0'''
        print("Resting login count...")
        self.login_attempts = 0


        # End Class

obj = User('pratik', 'sharma')
obj.describe_user()

obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.get_login_attempt()

obj.reset_login_attempts()
obj.get_login_attempt()