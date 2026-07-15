from pathlib import Path

from engine.text import vocabulary
from engine.text.vocabulary import build_vocabulary
from engine.autocomplete.autocomplete import AutocompleteEngine

_engine = None


def get_engine():
    global _engine

    if _engine is None:
        corpus_path = (
            Path(__file__).parents[2]
            / "engine"
            / "corpus"
            / "yoruba_sample.txt"
        )

        text = corpus_path.read_text(encoding="utf-8")

        vocabulary = build_vocabulary(text)

        _engine = AutocompleteEngine(vocabulary)

    return _engine