import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize Yoruba text while preserving tone marks
    and making comparisons case-insensitive.
    """
    return unicodedata.normalize("NFC", text).casefold()