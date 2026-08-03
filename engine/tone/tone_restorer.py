from engine.tone.tone_map import build_tone_map
from engine.text.tone_normalizer import strip_diacritics


class ToneRestorer:
    def __init__(self, vocabulary):
        self.tone_map = build_tone_map(vocabulary)

    def restore_word(self, word):
        key = strip_diacritics(word)
        matches = self.tone_map.get(key)

        if matches:
            return matches[0]   # Best candidate for now

        return word

    def restore_sentence(self, text):
        return " ".join(
            self.restore_word(word)
            for word in text.split()
        )