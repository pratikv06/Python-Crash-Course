fav_lang = {
    'pratik': 'python',
    'amit': 'java',
    'anand': 'php',
    'nilesh': 'oracle',
    'vishal': 'go',
    'jayesh': 'php',
    'ajay': 'python'
}
print(">> Looping through key and value both:")
for key, value in fav_lang.items():
    print(key.title() +"'s favorite language is "+ value.title())

print("\n>> Looping through key:")
friends = ['pratik', 'vishal']
for name in fav_lang.keys(): # default behaviour, so we can omit '.keys()'
    print(name.title())
    if name in friends:
        print("Hi "+ name.title() +", I see your favorite language is "+ fav_lang[name].title())

print("\n> check if person is not in dictionary")
if 'ratnesh' not in fav_lang.keys():
    print("Ratnesh, please provide your favorite language!")

print("\n> Let sort the dictonary by key")
for name in sorted(fav_lang):   # key is sorted temporary
    print(name.title() + ", Thank you for taking Poll!")

print("\n>> Looping through value:")
print(">List of all language in the list")
for lang in fav_lang.values():    # values() function wull return only value from dictionary
    print("$ "+ lang.title())

print("> The list of language is not unique. let's make it unique")
for lang in set(fav_lang.values()):
    print("$ "+ lang.title())