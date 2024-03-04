import random
import string
from dictogram import Dictogram
from collections import deque

class MarkovChain(Dictogram):
    def __init__(self, word_list=None):
        self.markov_dict = {}
        self.word_list = word_list
        self.types = 0  
        self.tokens = 0 
        if word_list is not None:
            self.markov_chain()

    def markov_chain(self):
        queue = deque(maxlen=2)
        for word in self.word_list:
            queue.append(word)
            if len(queue) == 2:
                word_pair = tuple(queue)
                next_word_dict = self.markov_dict.get(word_pair, Dictogram())
                next_word = queue[-1]
                next_word_dict.add_count(next_word)
                self.markov_dict[word_pair] = next_word_dict

    def generate_sentence(self, max_words=20):
        sentence = []
        punctuation = ["!", "?", ".", "..."]
        queue = deque(maxlen=2)
        while len(sentence) < max_words:
            if len(queue) == 0:
                word_pair = random.choice(list(self.markov_dict.keys()))
            else:
                word_pair = tuple(queue)
            next_word_dict = self.markov_dict.get(word_pair)
            
            if next_word_dict is None:
                queue.clear()
            else:
                next_word = next_word_dict.sample()
            
            if next_word not in sentence:
                sentence.append(next_word)
                queue.append(next_word)

        sentence = " ".join(sentence)
        sentence = sentence.capitalize()
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))

        sentence += random.choice(punctuation)

        return sentence

    def print_markov_chain(self, num_samples=1):
        print("Markov chain samples:")
        for _ in range(num_samples):
            sentence = self.generate_sentence()
            print(sentence)
        print()


def main():
    word_list = open("data/sample_text.txt", "r").read().split()
    markov = MarkovChain(word_list)
    markov.print_markov_chain()

if __name__ == '__main__':
    main()