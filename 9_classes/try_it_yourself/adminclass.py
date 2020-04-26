import privilege

class Admin():
    '''Admimistrator accss'''
    def __init__(self, firstname, lastname, privileges):
        '''Initializing attribute'''
        self.first_name = firstname
        self.last_name = lastname
        self.privilege = privilege.Privilege(privileges)

    # Class Admin End