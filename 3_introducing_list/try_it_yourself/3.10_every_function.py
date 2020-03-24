"""
Problem:
Think of something you could store in a list. For example, you could make a 
list of mountains, rivers, countries, cities, languages, or anything else 
you’d like. Write a program that creates a list containing these items and then 
uses each function introduced in this chapter at least once.
"""
lang = ['english', 'hindi', 'english', 'gujarati', 'nepali','russian']

print("1. Displaying List:", lang)

print("2. Displaying Element a index 1:", lang[1].title())

print("3. Display element at last index:", lang[-1])

lang.append('marathi')
print("4. Adding element at last of the list:", lang)

lang.insert(3,'french')
print("5. Adding Element at index 3:", lang)

del lang[4]
print("6. Deleting value at index 4:", lang)

remove = lang.pop()
print("7. Removed Element from last of list:", remove)
print("   List:", lang)

remove = lang.pop(1)
print("8. Removed value at index 1:", remove)
print("   list:", lang)

lang.remove('english')
print("9. Deleting element using value:", lang)

lang.reverse()
print("10. Reversing a list:", lang)

print("11. Temp. sorting:", sorted(lang))

print("12. Reverse Temp. sorting:", sorted(lang, reverse=True))

lang.sort()
print("13. Sorting list:", lang)

lang.sort(reverse=True)
print("14. Reverse Sorting list:", lang)

print("15. Length of the list:", len(lang))