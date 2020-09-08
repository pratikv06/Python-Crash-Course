filename = 'file2_pi_million_digits.txt'
with open(filename) as file_contents:
    lines = file_contents.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(len(pi_string))

birthday = input("Enter your birthday, in the form 'ddmmyy': ")
if birthday in pi_string:
    print("Your Birthday appears in the first million digits of PI.")
else:
    print("Your Birthday does not appears in the first million digits of PI.")