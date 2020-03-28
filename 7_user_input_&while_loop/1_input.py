# input always treat every input as string
# to display data type use type() function

print(">> Taking input from user nad displaying the input message")
message = input("Enter Some Message: ") # Accept one argument, which is for prompting messages
print(message)
print(type(message))    # Getting type of variable

print("\n>> Passing variable in input function")
str = "If you tells us who you are, I will print a message for you!"
str += "\nEnter Your first name: "  # Appending string at the end of the variable
message = input(str)
print("Hello, "+ message)
print(type(message))

print(">> Converting string to integer")
age = int(input("How old are you: "))   # Converting string to integer, using int() function
print(age)
print(type(age))
print("Lets Check if your age is even or odd")
if age%2 == 0:
    print("Your age "+ str(age) +" is even.")
else:
    print("Your age "+ str(age) +" is odd.")
