from pathlib import Path


def load_corpus(folder="corpus"):
    text = ""

    for file in Path(folder).rglob("*.txt"):
        text += file.read_text(
            encoding="utf-8",
            errors="ignore"
        )
        text += "\n"

    return text