from pathlib import Path

from engine.ai.ngram import BigramModel

_model = None

BIGRAM = (
    Path(__file__).parents[2]
    / "engine"
    / "models"
    / "bigram.json"
)


def get_bigram():
    global _model

    if _model is None:
        model = BigramModel()
        model.load(BIGRAM)

        _model = model

    return _model