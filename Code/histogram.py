import random
import sys, random
from string import punctuation

class histo_word:
    def __init__(self, word, count):
        self.word = word
        self.count = count

def histogram(source_text):
    #take in source text as an argument

    #open the file
    file = open(source_text, 'r')

    #split the file into words
    words = file.read().split(" ")

    #create an empty dictionary with words as keys and counts as values
    dict = {}

    #loop through the words to remove punctuation and lowercase
    for word in words:
        word = word.lstrip(punctuation).rstrip(punctuation).lower()
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    for word in dict:
        print(f'{word} = {dict[word]}')

    unique_words(dict)


def unique_words(dict):
    #unique words = length of the dictionary
    print(f'Unique words: {len(dict)}')