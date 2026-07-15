from collections import Counter

from engine.text.tokenizer import tokenize
from engine.text.normalizer import normalize_text


def build_vocabulary(text: str):
    """
    Build a frequency dictionary from Yoruba text.
    """
    normalized = normalize_text(text)
    words = tokenize(normalized)
    return Counter(words)