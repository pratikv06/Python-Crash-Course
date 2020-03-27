print(">> Storing dictionary in a list")

alien_0 = {
    'color': 'green',
    'point': 5,
}
alien_1 = {
    'color': 'red',
    'point': 10,
}
alien_2 = {
    'color': 'yellow',
    'point': 15,
}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print(">> Storing list in dictionary")
pizzas = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("Order Summary:")
print("You ordered a "+ pizzas['crust'].title()+ "-crust pizza with the following topping")
for topping in pizzas['toppings']:
    print("\t"+ topping)

print("\n>> Storing dictionary in dictionary")
users = {
    'coolalien': {
        'firstname': 'nilesh',
        'lastname': 'yadav',
        'city': 'pune',
        'company': 'hdfc',
    },
    'gpool': {
        'firstname': 'gaurav',
        'lastname': 'sharma',
        'city': 'banglore',
        'company': 'axis',
    },
}
for userid, userinfo in users.items():
    print("User Id: "+ userid)
    fullname = userinfo['firstname'] +" "+ userinfo['lastname']
    location = userinfo['city']
    companyname = userinfo['company']
    print("\tFullname : "+ fullname.title())
    print("\tComapny Name : "+ companyname.title())
    print("\tLocation :"+ location.title())
