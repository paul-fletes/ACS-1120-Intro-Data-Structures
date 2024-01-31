import re
from collections import Counter
import argparse
from sample import random_word

def read_source_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_text = file.read()
    return source_text

def histogram(source_text):
    words = re.findall(r'\b\w+\b', source_text.lower())
    return Counter(words)

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

def print_full_histogram(histogram, sort_by=None):
    if sort_by == 'num':
      sorted_histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    else:
      sorted_histogram = sorted(histogram.items(), key=lambda x: x[0])

    for word, count in sorted_histogram:
        print(f"{word}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a word histogram from a source tex and sample random words.")
    parser.add_argument("source_text", help="Path to the source text file.")
    parser.add_argument("-s", "--sort", choices=["num", "alpha"], default=None,
                        help="Sort the histogram. 'numeric' for numeric sort, 'alpha' for alphabetical sort.")
    parser.add_argument("-r", "--random", action="store_true",
                        help="Sample a random word from the histogram.")
    args = parser.parse_args()

    # Read source text
    source_text = read_source_text(args.source_text)

    # Generate histogram
    word_histogram = histogram(source_text)

    # Example usage:
    print("Total Unique Words:", unique_words(word_histogram))
    print("Frequency of 'water':", frequency('water', word_histogram))

    # python3 histogram.py <source> -s <num | alpha>

  # Sample a random word if the -r flag is provided
    if args.random:
<<<<<<< HEAD
        # # Sample weights
        # word_weights = {'water': 10, 'red': 40, 'the': 20}
        # add 'weights=word_weights' to add custom weigting!
        sampled_word = random_word(word_histogram)
=======
        # Sample weights
        word_weights = {'water': 10, 'red': 40, 'the': 20}
        sampled_word = random_word(word_histogram, weights=word_weights)
>>>>>>> 842ba2b4f055bb8265d0e61da7e562c3c049230f
        print("\nSampled Random Word:", sampled_word)
    else:
    # Print the full histogram with sorting if -r flag is not provided
        print("\nFull Histogram:")
        print_full_histogram(word_histogram, sort_by=args.sort)
