import random

def random_word(histogram, weights=None):
    if weights is None:
        weights = {word: 1 for word in histogram.keys()}  # Default weights are all 1

    weighted_words = []
    for word, count in histogram.items():
        if word in weights and weights[word] > 0:
          weighted_words.extend([word] * weights[word])
    
    if weighted_words:
        selected_word = random.choice(weighted_words)
        return selected_word
    else:
        return None
