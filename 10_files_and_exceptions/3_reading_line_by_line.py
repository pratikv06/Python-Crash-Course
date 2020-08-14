filename = "file1_pi_digit.txt"
print("> Reading file line by line using for loop")
with open(filename) as file_object:
    for line in file_object:
        print(line)


print("\n> Removing extra line using rsplit")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n> Removing extra line using end in print")
with open(filename) as file_object:
    for line in file_object:
        print(line,end='')