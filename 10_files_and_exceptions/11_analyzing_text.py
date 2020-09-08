filename = 'file3_sample_text.txt'
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print(f'Sorry, the file `{filename}` does not exist...')
else:
    # Count the approximate words used in file
    words = content.split()
    num_words = len(words)
    print(f'The file `{filename}` has about {num_words} words.')