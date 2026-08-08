import json

from engine.models import VOCABULARY
from engine.autocomplete.autocomplete import AutocompleteEngine

_engine = None


def get_engine():
    global _engine

    if _engine is None:
        with VOCABULARY.open(encoding="utf-8") as f:
            vocabulary = json.load(f)

        _engine = AutocompleteEngine(vocabulary)

    return _engine