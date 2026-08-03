from engine.text.tone_normalizer import strip_diacritics


def build_tone_map(words):
    tone_map = {}

    for word in words:
        key = strip_diacritics(word)

        tone_map.setdefault(key, [])

        if word not in tone_map[key]:
            tone_map[key].append(word)

    return tone_map