print("Using range to create list of number:")
num = list(range(1,6))
print(num)

print("Store only Even Number:")
num1 = list(range(2,11,2))
# agrument 1 = start 
# argument 2 = end
# agrument 3 = increment/decrement by 
print(num1)

print("Store only odd Number in reverse order:")
num2 = list(range(9,0,-2))
print(num2)

print("Store square of number from 1 to 10:")
squares = [] # Create empty list
for value in range(1,11):
   squares.append(value**2)
print(squares)