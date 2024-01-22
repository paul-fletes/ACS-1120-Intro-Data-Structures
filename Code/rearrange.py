import sys
import random

def rearrange_words(words):
    random.shuffle(words)
    return ' '.join(words)

if __name__ == "__main__":
    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]

    if not arguments:
        print("Please provide words to rearrange.")
    else:
        # Call the function to rearrange the words
        rearranged_result = rearrange_words(arguments)
        print(rearranged_result)
