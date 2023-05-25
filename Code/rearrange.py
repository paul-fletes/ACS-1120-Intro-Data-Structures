import sys
import random

def rearrange_words(arg_list):
    word_list = arg_list[1:]
    random.shuffle(word_list)
    new_string = " ".join(word_list)
    return new_string

if __name__ == "__main__":
    new_string = rearrange_words(sys.argv)
    print(new_string)