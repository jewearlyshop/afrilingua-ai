import unicodedata


def strip_diacritics(text: str) -> str:
    """
    Remove Yoruba tone marks and combining accents while
    preserving base letters for comparison.
    """
    decomposed = unicodedata.normalize("NFD", text)

    stripped = "".join(
        ch
        for ch in decomposed
        if unicodedata.category(ch) != "Mn"
    )

    return unicodedata.normalize("NFC", stripped).lower()