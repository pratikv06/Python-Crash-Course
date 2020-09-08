# This will raise an error
# filename = 'newfile.txt'
# with open(filename) as f:
#     print(f.read())

# Handling the above error
filename = 'newfile.txt'
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print(f'Sorry, the file `{filename}` does not exist...')