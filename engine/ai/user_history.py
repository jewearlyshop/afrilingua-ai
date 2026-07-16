from collections import defaultdict, Counter


class UserHistory:
    def __init__(self):
        self.history = defaultdict(Counter)

    def record(self, previous_word, selected_word):
        self.history[previous_word][selected_word] += 1

    def predict(self, previous_word, limit=5):
        return [
            word
            for word, _ in self.history[previous_word].most_common(limit)
        ]