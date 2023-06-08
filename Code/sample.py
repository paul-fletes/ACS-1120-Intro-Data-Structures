import random
import sys
from string import punctuation

# set command line args to a variable
num_of_runs = int(sys.argv[1])

# generate a histogram from source text
def histogram(source_text):
    histogram = {}
    with open(source_text, 'r') as file:
        word_list = file.read().split(' ')
        for word in word_list:
            word = word.strip(punctuation).lower()
            if word in histogram.keys():
                histogram[word] += 1
            else:
                histogram[word] = 1
    return histogram

# generate total word count for the source text
def generate_total_word_count(histogram):
    weights = list(histogram.values())
    word_count = 0
    for weight in weights:
        word_count += weight
    return word_count

