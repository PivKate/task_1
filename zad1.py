import random

# Read the file
with open('file.txt', 'r') as file:
    filedata = file.read()


def scramble(word):
    if word[-1] == '.' or word[-1] == ',':
        letters = list(word[1:-2])
        random.shuffle(letters)
        return word[0] + ''.join(letters) + word[-2:]
    else:
        letters = list(word[1:-1])
        random.shuffle(letters)
        return word[0] + ''.join(letters) + word[-1]


new_text = ' '.join(scramble(word) for word in filedata.split())

# Write the file
with open('newfile.txt', 'w') as file:
    file.write(new_text)
