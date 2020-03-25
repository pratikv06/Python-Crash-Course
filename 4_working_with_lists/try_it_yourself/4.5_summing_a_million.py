"""
Problem:
make a list of the numbers from one to one million, and then use min() and max() 
to make sure your list actually starts at one and ends at one million. Also, 
use the sum() function to see how quickly Python can add a million numbers.
"""

num = list(range(1,1000001))
print("Minimum:", min(num))
print("Maximum:", max(num))
print("Sum:", sum(num))