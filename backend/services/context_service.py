from engine.text.corpus_loader import load_corpus
from engine.ai.ngram import BigramModel

_model = None


def get_bigram():
    global _model

    if _model is None:
        text = load_corpus()

        model = BigramModel()
        model.train(text)

        _model = model

    return _model