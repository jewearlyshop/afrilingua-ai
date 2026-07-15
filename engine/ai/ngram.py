from collections import defaultdict, Counter


class BigramModel:
    def __init__(self):
        self.model = defaultdict(Counter)

    def train(self, words):
        for first, second in zip(words, words[1:]):
            self.model[first][second] += 1

    def predict(self, word, limit=5):
        predictions = self.model.get(word, {})
        return [
            next_word
            for next_word, _ in predictions.most_common(limit)
        ]