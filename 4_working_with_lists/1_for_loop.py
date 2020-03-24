"""
> for loop will take one value at a time from magicians list and store that value 
in magician variable till the magicians list came to an end.
> There is no concept of brackets
> 'Colon' denote the start of the bracket (Goto: line 13 and 17)
> As for the body of the loop it is denoted using "indentation"
> indentation is not for show (Goto: line 14 and 18)
> To end loop remove the indentation (Goto: line 16 and 21)
"""

magicians = ['alice', 'david', 'carolina'] 
print("Loop 1:")
for magician in magicians: 
   print(magician)

print("Loop 2:")
for magician in magicians: 
   print(magician.title() + ", that was a great trick!")
   print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")