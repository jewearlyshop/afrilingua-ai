import re
import unicodedata


def tokenize(text: str):
    """
    Tokenize Yoruba text while preserving combining tone marks.
    """
    tokens = []
    current = ""

    for char in unicodedata.normalize("NFC", text):
        category = unicodedata.category(char)

        # Letters
        if category.startswith("L"):
            current += char

        # Combining marks (tone marks)
        elif category.startswith("M") and current:
            current += char

        else:
            if current:
                tokens.append(current)
                current = ""

    if current:
        tokens.append(current)

    return tokens