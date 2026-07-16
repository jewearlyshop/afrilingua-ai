from collections import defaultdict, Counter

from engine.text.tokenizer import tokenize
from engine.text.normalizer import normalize_text


class BigramModel:
    def __init__(self):
        self.model = defaultdict(Counter)

    def train(self, text):
        words = tokenize(normalize_text(text))

        for first, second in zip(words, words[1:]):
            self.model[first][second] += 1

    def predict(self, previous_word, limit=5):
        previous_word = normalize_text(previous_word)

        return [
            word
            for word, _ in self.model[previous_word].most_common(limit)
        ]