"""
Problem:
Store a person’s name, and include some whitespace characters at the beginning 
and end of the name. Make sure you use each character combination, "\t" and 
"\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print
the name using each of the three stripping functions, lstrip(),  rstrip(), and 
strip().
"""

name = "\t\tEric\n\t"
print("Original name :")
print(name)

print("Left strip :")
print(name.lstrip())

print("Right strip :")
print(name.rstrip())

print("Strip :")
print(name.strip())