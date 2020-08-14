print("> Storing file data in list")
filename = 'file1_pi_digit.txt'

with open(filename) as file_contents:
    lines = file_contents.readlines()

for line in lines:
    print(line.rstrip())


# NOTE:
# readlines() - read one line at a time from files