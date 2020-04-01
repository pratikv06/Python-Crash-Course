"""
Problem:
Start with a copy of user_profile.py. Build a profile of yourself by calling 
build_profile(), using your first and last names and three other key-value 
pairs that describe you.
"""
def build_profile(first, last, **user_info): # ** for dictionary
    """Build dictionary containing user information"""
    profile = {
        'first_name': first,
        'last_name': last
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('pratik', 'vishwakarma',
                            location= 'pune', job= 'system programmer', 
                            experience= '5 years')
print(user_profile)