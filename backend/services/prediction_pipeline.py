from backend.services.prediction_service import get_engine
from backend.services.context_service import get_bigram
from engine.text.normalizer import normalize_text


class PredictionPipeline:
    def __init__(self):
        self.engine = get_engine()
        self.bigram = get_bigram()

    def predict(self, text: str):
        # Preserve the original text to detect a trailing space
        original_text = text

        # Remove only leading spaces
        text = text.lstrip()

        if not text:
            return []

        words = text.split()

        # User has completed a word and typed a space
        if original_text.endswith(" ") and words:
            previous = normalize_text(words[-1])
            return self.bigram.predict(previous)

        # User is typing the current word
        current = normalize_text(words[-1])
        return self.engine.suggest(current)