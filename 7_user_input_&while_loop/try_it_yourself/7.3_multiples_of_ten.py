"""
Problem:
Ask the user for a number, and then report whether the number is a multiple of 
10 or not.
"""

number = int(input("Enter a number : "))
if number%10 == 0:
    print("The provided number is multiple of 10.")
else:
    print("The provided number is not a multiple of ten.")