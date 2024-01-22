import sys
import random

def read_words_file(path):
  with open(path, 'r') as file:
    words = file.read().splitlines()
  return words

def generate_sentence(word_list, num_words):
  selected_words = random.sample(word_list, num_words)
  sentence = ' '.join(selected_words)
  return sentence

if __name__ == "__main__":
  words_file_path = "/usr/share/dict/words"

  if len(sys.argv) != 2:
    print("Usage: python3 dictionary_words.py <number_of_words>")
    sys.exit(1)
  
  try:
    num_words = int(sys.argv[1])
  except ValueError:
    print("Please provide a valid integer for the number of words.")
    sys.exit(1)
  
  word_list = read_words_file(words_file_path)

  generated_sentence = generate_sentence(word_list, num_words)
  print(generated_sentence)
  
