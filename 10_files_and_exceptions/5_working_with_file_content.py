print("> Storing file data in list")
filename = 'file1_pi_digit.txt'

with open(filename) as file_contents:
    lines = file_contents.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# Note:
# rstrip() - remove space and new line from right of string 
# lstrip() - remove space from left of string
# strip() - remove sapce from both end

print("\n> Printing only first 10 digit")
print(pi_string[:10] + "...")

print(pi_string, type(pi_string), len(pi_string))

pi_string = float(pi_string)
print(pi_string, type(pi_string),)

# print(len(pi_string))
# Note: 
# we cannot find lenght of float, 
# solution: convert it into str then substract one from it