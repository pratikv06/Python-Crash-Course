"""
Problem:
Imagine an alien was just shot down in a game . Create a variable called 
alien_color and assign it a value of 'green', 'yellow', or 'red'.
> Write an if statement to test whether the alien’s color is green. If it is, 
  print a message that the player just earned 5 points.
> Write one version of this program that passes the if test and another that
  fails. (The version that fails will have no output.)
"""
alien_color = ['green', 'yellow', 'red']

# if is true
color = 'green'
if color in alien_color:
  print("Player earned 5 Points!")

# if is flase
color = 'blue'
if color in alien_color:
  print("Player earnd 5 Points!")