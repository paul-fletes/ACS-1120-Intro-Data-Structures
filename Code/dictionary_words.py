import random
import sys

# take in argument for number of words to pull from file
num_words = int(sys.argv[1])

# open the file and separate each word into a list
dict = open('/usr/share/dict/words', 'r')
lines = dict.read().splitlines()

# create a list to store the words
random_words = []

# add n random words into list
num = 0
while num < num_words:
    line = lines[random.randint(0, len(lines))]
    random_words.append(line)
    num += 1

# print the list of random words as a "sentence"
random_sentence = " ".join(random_words)
print(random_sentence)

# close the file
dict.close()
