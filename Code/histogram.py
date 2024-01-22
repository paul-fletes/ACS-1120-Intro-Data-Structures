import re
from collections import Counter
import argparse

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
      sorted_histogram = sorted(histogram.items())

    for word, count in sorted_histogram:
        print(f"{word}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a word histogram from a source text.")
    parser.add_argument("source_text", help="Path to the source text file.")
    parser.add_argument("-s", "--sort", choices=["num", "alpha"], default=None,
                        help="Sort the histogram. 'numeric' for numeric sort, 'alpha' for alphabetical sort.")
    args = parser.parse_args()

    # Read source text
    source_text = read_source_text(args.source_text)

    # Generate histogram
    word_histogram = histogram(source_text)

    # Example usage:
    print("Total Unique Words:", unique_words(word_histogram))
    print("Frequency of 'water':", frequency('water', word_histogram))

    # Print full histogram sorted by count:
    # print("\nFull Histogram (sorted by count):")
    # print_full_histogram(word_histogram, sort_by='count')

    # Print full histogram sorted alphabetically:
    # print("\nFull Histogram (sorted alphabetically):")
    # print_full_histogram(word_histogram)

    print("\nFull Histogram:")
    print_full_histogram(word_histogram, sort_by=args.sort)
