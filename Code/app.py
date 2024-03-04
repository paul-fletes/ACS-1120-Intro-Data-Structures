"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from histogram import histogram, random_word, read_source_text
from markov import MarkovChain


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
# Read source text and generate histogram
source_text = read_source_text('data/source_text.txt')
word_histogram = histogram(source_text)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    with open('data/source_text.txt', 'r') as file:
        word_list = file.read().split()
    markov = MarkovChain(word_list=word_list).generate_sentence(max_words=20)
    return render_template('index.html', markov=markov)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
