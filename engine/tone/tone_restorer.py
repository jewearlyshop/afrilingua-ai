import json

from engine.models import TONE
from engine.text.tone_normalizer import strip_diacritics


class ToneRestorer:
    def __init__(self):
        with TONE.open(encoding="utf-8") as f:
            self.tone_map = json.load(f)

    def restore_word(self, word):
        key = strip_diacritics(word)

        matches = self.tone_map.get(key)

        if matches:
            return matches[0]

        return word

    def restore_sentence(self, text):
        return " ".join(
            self.restore_word(word)
            for word in text.split()
        )