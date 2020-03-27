"""
Problem:
Use the dictionay fav_lang.
> Make a list of people who should take the favorite languages poll. Include
  some names that are already in the dictionary and some that are not. 
> Loop through the list of people who should take the poll. If they have already 
  taken the poll, print a message thanking them for responding. If they have not 
  yet taken the poll, print a message inviting them to take the poll.
"""
fav_lang = {
    'pratik': 'python',
    'amit': 'java servlet',
    'rahul': 'c++',
    'anand': 'php',
}
peoples = ['pratik', 'jay', 'sumit', 'amit', 'ritik']

for people in peoples:
    if people in fav_lang:
        print("Thank you for responding "+ people.title())
    else:
        print(people.title() +", are you interested in taking our poll?")