"""
Problem:
Write a series of conditional tests. Print a statement describing each test and 
your prediction for the results of each test. Your code should look something 
like this:
--------------------------------------------------------------------------------
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
--------------------------------------------------------------------------------
> Look closely at your results, and make sure you understand why each line 
  evaluates to True or False.
> Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 
  tests evaluate to False.
"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

age = 21
print("\nIs age == 21? I predict True.")
print(age == 21)
print("Is age == 20? I predict False.")
print(age == 20)

print("\nIs age > 21? I predict True.")
print(age > 21)
print("Is age < 21? I predict False.")
print(age <21)

print("\nIs age > 20 and age < 30? I predict True.")
print(age > 20 and age < 30)
print("Is age < 20 and age > 30? I predict False.")
print(age < 20 and age > 30)

print("\nIs age != 20? I predict True")
print(age != 20)
print("Is age != 21? I predict False.")
print(age != 21)