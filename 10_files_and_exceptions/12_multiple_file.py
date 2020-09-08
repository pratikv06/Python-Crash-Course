def word_counts(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        # print(f'Sorry, the file `{filename}` does not exist...')

        # don't want to display exception error 
        pass
    else:
        # Count the approximate words used in file
        words = content.split()
        num_words = len(words)
        print(f'The file `{filename}` has about {num_words} words.')

filenames = ['file1_pi_digit.txt', 'new_sample.txt', 'file2_pi_million_digits.txt', 'file.txt']
for f in filenames:
    word_counts(f)