with open('file1_pi_digit.txt') as file_object:
    contents = file_object.read()
    print(type(contents))
    print(contents)

    print("\nRemoving Extra Line:")
    print(contents.rstrip(), end='')

"""
> open()
    - one argument: file name with extension
    - return: object representing file 

> `with` will handle opening and closing of file

> read()
    - read entire content of the file

> rstrip()
    - This wil remove all the blank space from the text in file

> end=''
    - This will prevent enter to new line after executing print statement
"""