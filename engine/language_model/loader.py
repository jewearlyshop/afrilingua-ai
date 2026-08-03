import json
from pathlib import Path


class LanguageModel:

    def __init__(self):
        folder = Path(__file__).parent

        with open(folder / "bigrams.json", encoding="utf-8") as f:
            self.bigrams = json.load(f)

        with open(folder / "trigrams.json", encoding="utf-8") as f:
            self.trigrams = json.load(f)

    def next_words(self, *previous_words, limit=5):
        scores = {}

        # Use trigrams if two previous words are available
        if len(previous_words) >= 2:
            prefix = f"{previous_words[-2]} {previous_words[-1]} "

            for phrase, count in self.trigrams.items():
                if phrase.startswith(prefix):
                    next_word = phrase.split()[2]
                    scores[next_word] = count

        # Fall back to bigrams
        if not scores and len(previous_words) >= 1:
            prefix = previous_words[-1] + " "

            for phrase, count in self.bigrams.items():
                if phrase.startswith(prefix):
                    next_word = phrase.split()[1]
                    scores[next_word] = count

        return sorted(
            scores,
            key=scores.get,
            reverse=True
        )[:limit]