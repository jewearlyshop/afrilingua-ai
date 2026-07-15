from tone_map import build_tone_map


class ToneRestorer:
    def __init__(self, vocabulary):
        self.tone_map = build_tone_map(vocabulary)

    def restore(self, word):
        key = word.lower()
        return self.tone_map.get(key, [])