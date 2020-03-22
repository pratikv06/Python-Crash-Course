print("*** Integers ***")
print("2 + 3 =", 2+3) # add
print("3 - 2 =", 3-2) # subtract
print("2 * 3 =", 2*3) # multiply
print("3 / 2 =", 3/2) # divide
print("3 ** 2 =", 3**2) # exponents 
print("3 ** 3 =", 3**3)
print("10 ** 6 =", 10**6)
print("2 + 3 * 4 =", (2+3*4)) # expression
print("(2 + 3) * 4 =", ((2+3)*4)) 

print("\n*** Floats ***")
print("0.1 + 0.1 =", 0.1+0.1)
print("0.2 + 0.2 =", 0.2+0.2)
print("2 * 0.1 =", 2*0.1)
print("2 * 0.2 =", 2*0.2)
print("0.2 + 0.1 =", 0.2+0.1) # precising result
print("3 * 0.1 =", 3*0.1)

print("\nAvoiding Type Errors with the str() Function")
age = 23
message = "Happy "+ str(age) +"rd Birthday!" # without str, it will thorw typrerror
print(message)