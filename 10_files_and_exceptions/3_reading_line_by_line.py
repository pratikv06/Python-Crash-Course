filename = "file1_pi_digit.txt"
print("> Reading file line by line using for loop")
with open(filename) as file_object:
    for line in file_object:
        print(line)
# two new line add
# - one from file 
# - another one from print

print("\n> Removing extra line from file using rsplit")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n> Removing extra line from print using end")
with open(filename) as file_object:
    for line in file_object:
        print(line,end='')