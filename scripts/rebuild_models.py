from pathlib import Path
from engine.vocabulary.builder import build_vocabulary



ROOT = Path(__file__).resolve().parent.parent

CORPUS = ROOT / "corpus"

VOCAB = (
    ROOT
    / "engine"
    / "vocabulary"
    / "vocabulary.json"
)
print("Building vocabulary...")

build_vocabulary(
    CORPUS,
    VOCAB,
)

from engine.tone.builder import build_tone_dictionary

TONE = (
    ROOT
    / "engine"
    / "tone"
    / "tone_dictionary.json"
)
print("Building tone dictionary...")

build_tone_dictionary(
    VOCAB,
    TONE,
)


print("Done.")