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