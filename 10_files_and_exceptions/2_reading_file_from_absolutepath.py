print("> Reading file using absolute path:")

filepath = r'D:\Pratik\Practice\Python\Python Crash Course\10_files_and_exceptions\file1_pi_digit.txt'

with open(filepath) as file_object:
    contents = file_object.read()
    print(contents)

# Note:
# Whenever reading the content of the file it will enter new line at the end of 
# the line