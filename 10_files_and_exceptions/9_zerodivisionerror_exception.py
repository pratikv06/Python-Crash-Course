# print(">> Exception ")
# print(5/0)

print("> Example of try-except")
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't Divide by ZERO")

# Put the line causing error in try block
# If try cause error then except block will run,
# otherwise it will skip except block

print("\n> Example of try-except-else with user input")
print("Give me two number, and I'll divide them.")
print("press 'q' to quit")

while True:
    number_one = input("First Number: ")
    if number_one.lower() == 'q':
        break
    number_two = input("Second Number: ")
    if number_two.lower() == 'q':
        break
    try:
        answer = int(number_one) / int(number_two)
    except:
        print("You can't Divide Zero!")
    else:
        print(f"Answer: {answer}")


# else will run only if try run successfully