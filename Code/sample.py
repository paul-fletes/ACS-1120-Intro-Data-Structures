import random
import sys
from string import punctuation

# set command line args to a variable
num_of_runs = int(sys.argv[1])

# generate a histogram from source text
def generate_histogram(source_text):
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

# generate a random word from the source text
def generate_random_word():
    histogram = generate_histogram('text.txt')
    keys = list(histogram.keys())
    weights = list(histogram.values())
    return random.choices(keys, weights=weights)[0]

def unique_words():
    histogram = generate_histogram('text.txt')
    return len(histogram.keys())

def frequency_total_words(histogram):
    return list(histogram.list())

def print_frequency(histogram):
    for word in histogram:
        print(f'{word} = {histogram[word]}')

def collect_stats(num_of_runs, word):
    unique_word_count = 0
    random_words = []
    random_words_histogram = {}
    for i in range(num_of_runs):
        random_words.append(generate_random_word())
    for word in random_words:
        if word in random_words_histogram.keys():
            random_words_histogram[word] += 1
        else:
            random_words_histogram[word] = 1
    return random_words_histogram

def get_probability(histogram):
    total = generate_total_word_count(histogram)
    new_histogram = {}
    for key, value in histogram.items():
        new_histogram[key] = (value / total)
    return new_histogram

def print_probability(histogram):
    new_histogram = get_probability(histogram)
    for key, value in histogram.items():
        print(f'{key} = {value}')

histogram = collect_stats(num_of_runs, "red")
print_frequency(histogram)
print_probability(histogram)

    