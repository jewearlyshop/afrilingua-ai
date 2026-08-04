from engine.text.corpus_loader import load_corpus
from engine.text.vocabulary import build_vocabulary
from engine.autocomplete.autocomplete import AutocompleteEngine

_engine = None


def get_engine():
    global _engine

    if _engine is None:
        text = load_corpus()

        vocabulary = build_vocabulary(text)

        _engine = AutocompleteEngine(vocabulary)

    return _engine