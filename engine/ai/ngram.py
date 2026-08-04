from importlib.resources import path
from os import path
import json
from pathlib import Path

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
    def save(self, output_file):
        path = Path(output_file)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        data = {
            word: dict(counter)
            for word, counter in self.model.items()
        }

        with path.open("w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )
    def load(self, input_file):
        path = Path(input_file)

        with path.open(encoding="utf-8") as f:
            data = json.load(f)

        self.model = defaultdict(Counter)

        for word, counts in data.items():
            self.model[word] = Counter(counts)    