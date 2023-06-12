import random
import sys
from string import punctuation

class Sampling:
	def __init__(self, source_text, number_of_runs):
		self.source_text = source_text
		self.number_of_runs = number_of_runs
		self.random_words = []
		self.histogram = self._generate_histogram()
		self.random_words_histogram = self.collect_stats()		
		self.total = self._generate_total_word_count()

	def _generate_histogram(self):
		histogram = {}
		with open(self.source_text, 'r') as file:
			word_list = file.read().split(' ')
			for word in word_list:
				word = word.strip(punctuation).lower() 
				if word in histogram.keys():
					histogram[word] += 1
				else:
					histogram[word] = 1
		return histogram

	def _generate_total_word_count(self):
		weights = list(self.random_words_histogram.values())
		word_count = 0
		for weight in weights: 
			word_count += weight
		return word_count 
	
	def _generate_random_word(self):
		keys = list(self.histogram.keys())
		values = list(self.histogram.values())
		return random.choices(keys, weights=values)[0]

	def _unique_words(self):
		return len(self.histogram.keys())

	def frequency_of_all_words(histogram):
		return list(histogram.items())
		
	def collect_stats(self):
		random_words_histogram = {}
		for x in range(self.number_of_runs):
			self.random_words.append(self._generate_random_word())
			for word in self.random_words:
				if word in random_words_histogram.keys():
					random_words_histogram[word] += 1
				else:
					random_words_histogram[word] = 1
		return random_words_histogram
		
	def print_frequency(self):
		for word in self.random_words_histogram:
			print(word , self.random_words_histogram.get(word, 0)) 

	def print_probability(self):
		new_histogram = {}
		for key, value in self.random_words_histogram.items():
			new_histogram[key] = (value/self.total)
		for key, value in new_histogram.items(): 
			print(f"{key}: {value}")


# set command line arguments to a variable
number_of_runs = int(sys.argv[1])
new_sample = Sampling('text.txt', number_of_runs)
new_sample.print_frequency()
new_sample.print_probability()