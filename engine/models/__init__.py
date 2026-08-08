from pathlib import Path

MODELS = Path(__file__).parent

VOCABULARY = MODELS / "vocabulary.json"
BIGRAM = MODELS / "bigram.json"
TONE = MODELS / "tone_dictionary.json"
TRIGRAM = MODELS / "trigram.json"