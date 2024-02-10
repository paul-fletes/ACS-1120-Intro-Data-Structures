from collections import defaultdict
import random

def build_markov_chain(corpus):
    markov_chain = defaultdict(dict)
    words = corpus.split()  # Split the corpus into words
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in markov_chain:
            markov_chain[current_word] = {}
        if next_word not in markov_chain[current_word]:
            markov_chain[current_word][next_word] = 0
        markov_chain[current_word][next_word] += 1
    return markov_chain

def random_walk(markov_chain, num_words):
    sentence = []
    for _ in range(num_words):
        if not sentence:
            current_word = random.choice(list(markov_chain.keys()))  # Start with a random initial word
        else:
            current_word = sentence[-1]
        
        # Check if the current word has transitions
        if current_word not in markov_chain or not markov_chain[current_word]:
            current_word = random.choice(list(markov_chain.keys()))  # Choose a new random initial word
        
        next_word = random.choices(
            list(markov_chain[current_word].keys()),
            weights=markov_chain[current_word].values()
        )[0]
        
        sentence.append(next_word)

    return ' '.join(sentence)

# Example usage:
corpus = "Red and Slim found the two strange little animals the morning after they heard the thunder sounds."
markov_chain = build_markov_chain(corpus)
generated_sentence = random_walk(markov_chain, num_words=10)
print(generated_sentence)