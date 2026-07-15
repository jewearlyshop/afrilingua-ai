import unicodedata


def strip_tones(text: str) -> str:
    """
    Remove combining tone marks while preserving Yoruba letters.
    Example:
        ọmọ -> omo
        ilé -> ile
    """
    text = unicodedata.normalize("NFD", text)

    result = []

    for ch in text:
        if unicodedata.category(ch) != "Mn":
            result.append(ch)

    text = "".join(result)

    # Restore Yoruba letters after removing combining marks
    return (
        text.replace("ọ", "o")
            .replace("Ọ", "O")
            .replace("ẹ", "e")
            .replace("Ẹ", "E")
    )


def build_tone_map(words):
    tone_map = {}

    for word in words:
        key = strip_tones(word)

        tone_map.setdefault(key, [])

        if word not in tone_map[key]:
            tone_map[key].append(word)

    return tone_map