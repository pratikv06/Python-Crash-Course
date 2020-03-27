fav_lang = {
    'pratik': ['python', 'php', 'javascript'],
    'gaurav': ['c', '.net'],
    'heem': ['java', 'python'],
    'rajneesh': ['andriod', 'java', 'php', 'oracle']
}

for name, lang in fav_lang.items():
    print("\n"+ name.title()+ "'s favorite language is")
    for l in lang:
        print("> "+ l.title())