from pathlib import Path

from engine.ai.ngram import BigramModel

_model = None


def get_bigram():
    global _model

    if _model is None:
        corpus = (
            Path(__file__).parents[2]
            / "engine"
            / "corpus"
            / "yoruba_sample.txt"
        )

        text = corpus.read_text(
            encoding="utf-8"
        )

        model = BigramModel()
        model.train(text)

        _model = model

    return _model