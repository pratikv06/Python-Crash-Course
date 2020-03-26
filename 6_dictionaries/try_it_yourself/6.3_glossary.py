"""
Problem:
A Python dictionary can be used to model an actual dictionary. However, to 
avoid confusion, let’s call it a glossary.
> Think of five programming words you’ve learned about in the previous chapters. 
  Use these words as the keys in your glossary, and store their meanings as 
  values.
> Print each word and its meaning as neatly formatted output. You might print 
  the word followed by a colon and then its meaning, or print the word on one 
  line and then print its meaning indented on a second line. Use the newline 
  character (\n) to insert a blank line between each word-meaning pair in your 
  output.
"""
glossary = {
    'programming': 'programming is the process of creating a set of instructions that tell a computer how to perform a task.',
    'list': 'list is a collection which is ordered and changeable.',
    'tuple': 'tuple is a collection which is ordered and unchangeable.',
    'set': 'set is a collection which is unordered and unindexed.',
    'dictionary': 'dictionary is a collection which is unordered, changeable and indexed.',
}

for key in glossary:
    print(key.title() +" its meaning \n"+ glossary[key])