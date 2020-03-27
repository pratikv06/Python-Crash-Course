"""
Problem:
Now that you know how to loop through a dictionary, clean up the code from 
Exercise 6-3 by replacing your series of print statements with a loop that 
runs through the dictionary’s keys and values. When you’re sure that your 
loop works, add five more Python terms to your glossary. When you run your 
program again, these new words and meanings should automatically be included 
in the output.
"""

glossary = {
    'programming': 'programming is the process of creating a set of instructions that tell a computer how to perform a task.',
    'list': 'list is a collection which is ordered and changeable.',
    'tuple': 'tuple is a collection which is ordered and unchangeable.',
    'set': 'set is a collection which is unordered and unindexed.',
    'dictionary': 'dictionary is a collection which is unordered, changeable and indexed.',
}
glossary['python'] = 'Python is an interpreted, high-level, general-purpose programming language.'
glossary['interpreter'] = 'Interpreter is a program that executes instructions written in a high-level language.'
glossary['compiler'] = 'A compiler is a computer program that translates computer code written in one programming language into another language.'
glossary['loop'] = 'Loop is used for iterating over a sequence.'
glossary['string'] = 'String literals in python are surrounded by either single quotation marks, or double quotation marks.'

for word, meaning in glossary.items():
    print(word.title() +" meaning:\n"+ meaning)