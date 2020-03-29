print(">> Moving items from one list to another")
unconfirmed_user = ['amit', 'vishal', 'altaf']
confirmed_user = []
while unconfirmed_user:
    user = unconfirmed_user.pop()
    print("Verifying user : "+ user.title())
    confirmed_user.append(user)
print("Displying the Conformed User: ")
for user in confirmed_user:
    print("\t> "+ user.title())


print("\n>> Removing all instance of specific value from a list")
pets = ['dog', 'cat', 'rabbit', 'dog', 'rabbit', 'dog', 'cat', 'dog']
print("Pet list: ", pets)
print("Let remove all the `dog` instances")
while 'dog' in pets:
    pets.remove('dog')
print("Updated List :", pets)