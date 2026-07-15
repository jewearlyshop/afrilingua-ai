from backend.services.prediction_service import get_engine

from engine.text.normalizer import normalize_text

class PredictionPipeline:
    def __init__(self):
        self.engine = get_engine()

    def predict(self, text: str):
        text = text.strip()

        if not text:
            return []

        # Only autocomplete the last word
        last_word = normalize_text(text.split()[-1])

        return self.engine.suggest(last_word)

        