from backend.services.prediction_service import get_engine
from backend.services.context_service import get_bigram
from engine.text.normalizer import normalize_text


class PredictionPipeline:
    def __init__(self):
        self.engine = get_engine()
        self.bigram = get_bigram()

    def predict(self, text: str):
        original = text

        text = text.lstrip()

        if not text:
            return []

        words = text.split()

        # Predict next word after a completed word
        if original.endswith(" "):
            previous = normalize_text(words[-1])
            return self.bigram.predict(previous)

        # Typing the first word
        if len(words) == 1:
            current = normalize_text(words[0])
            return self.engine.suggest(current)

        previous = normalize_text(words[-2])
        current = normalize_text(words[-1])

        context = self.bigram.predict(previous)

        filtered = [
            word
            for word in context
            if word.startswith(current)
        ]

        if filtered:
            return filtered

        return self.engine.suggest(current)