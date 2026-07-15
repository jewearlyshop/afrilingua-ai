import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize Yoruba text to NFC form.
    """
    return unicodedata.normalize("NFC", text)