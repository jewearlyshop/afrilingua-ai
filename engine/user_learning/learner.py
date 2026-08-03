import json
from pathlib import Path


class UserLearner:

    def __init__(self):
        self.file = Path(__file__).parent / "user_history.json"

        try:
            with open(self.file, encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}

    def learn(self, word):
        self.data[word] = self.data.get(word, 0) + 1

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                self.data,
                f,
                ensure_ascii=False,
                indent=4,
            )

    def predict(self, prefix="", limit=5):
        candidates = {
            word: count
            for word, count in self.data.items()
            if word.startswith(prefix)
        }

        return sorted(
            candidates,
            key=candidates.get,
            reverse=True
        )[:limit]