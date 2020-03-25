# - An immutable list is called a tuples
# - Parenthese i.e. '(' and ')' indicate tuples
# - Its element can be access by using index value

dimension = (200, 50)
print("Access tuple by index")
print("Value at index 0:", dimension[0])
print("value at index 1:", dimension[1])

print("Looping through tuples:")
for dim in dimension:
   print(">", dim)


# As tuples are immutable 
# let try to change its value and see what happen
dimension[0] = 250