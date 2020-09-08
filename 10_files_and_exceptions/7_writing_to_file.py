filename = 'output.txt'

with open(filename, 'w') as f:
    f.write("Python is awesome.\n")
    f.write("Python is Interpreted Language.\n")
    
# Note:
# We have to manually enter the new line 
# otherwise writr will continue to add string in same line

# If run this program again, it will rewrite the content in the file