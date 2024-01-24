import random

def random_word(histogram):
  all_words = list(histogram.keys())
  selected_word = random.choice(all_words)
  return selected_word