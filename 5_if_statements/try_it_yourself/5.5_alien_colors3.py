"""
Problem:
Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
> If the alien is green, print a message that the player earned 5 points.	
> If the alien is yellow, print a message that the player earned 10 points.
> If the alien is red, print a message that the player earned 15 points.
> Write three versions of this program, making sure each message is printed 
  for the appropriate color alien.
"""

alien_color = 'green'
if alien_color == 'green':
   print("Player earn 5 Points!")
elif alien_color == 'yellow':
   print("Player earn 10 Points!")
elif alien_color == 'red':
   print("Player earn 15 Points!")

alien_color = 'yellow'
if alien_color == 'green':
   print("Player earn 5 Points!")
elif alien_color == 'yellow':
   print("Player earn 10 Points!")
elif alien_color == 'red':
   print("Player earn 15 Points!")

alien_color = 'red'
if alien_color == 'green':
   print("Player earn 5 Points!")
elif alien_color == 'yellow':
   print("Player earn 10 Points!")
elif alien_color == 'red':
   print("Player earn 15 Points!")