import random
import sys

# # take in argument for number of words to pull from file
result = sys.argv[1]
number = int(result)

# # open the file and separate each word into a list
# dict = open('/usr/share/dict/words', 'r')
# lines = dict.read().splitlines()

# # create a list to store the words
# random_words = []

# # add n random words into list
# num = 0
# while num < num_words:
#     line = lines[random.randint(0, len(lines))]
#     random_words.append(line)
#     num += 1

# # print the list of random words as a "sentence"
# random_sentence = " ".join(random_words)
# print(random_sentence)

# # close the file
# dict.close()

class Dictionary():
	def __init__(self, result, number):
		self.result = result
		self.number = number

	def _read_file(self):
		with open('Code/words.txt') as file:
			data = file.readlines()
			random_words = random.sample(data, len(data))
			for i in range(0, number): 
				print(random_words[i].strip(), end = " ")