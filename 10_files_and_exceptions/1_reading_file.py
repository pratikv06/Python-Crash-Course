with open("file1_pi_digit.txt") as file_object:
    contents = file_object.read()
    print(contents)

"""
> open()
    - one argument: file name with extension
    - return: object representing file 

> `with` will handle opening and closing of file

> read()
    - read entire content of the file
"""