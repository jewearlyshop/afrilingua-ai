from engine.ai.ngram import BigramModel
from engine.models import BIGRAM

_model = None


def get_bigram():
    global _model

    if _model is None:
        model = BigramModel()
        model.load(BIGRAM)
        _model = model

    return _model