from collections import Counter
from pathlib import Path
import json

from engine.text.tokenizer import tokenize
from engine.text.normalizer import normalize_text


def build_vocabulary(corpus_dir, output_file):
    counter = Counter()

    corpus_path = Path(corpus_dir)

    for file in corpus_path.rglob("*.txt"):
        with file.open("r", encoding="utf-8") as f:
            text = f.read()

        words = tokenize(
            normalize_text(text)
        )

        counter.update(words)

    MIN_FREQUENCY = 1

    counter = Counter({
        word: count
        for word, count in counter.items()
        if count >= MIN_FREQUENCY
    })

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(counter, f, ensure_ascii=False, indent=4)

    print(f"Processed {len(list(corpus_path.rglob('*.txt')))} files.")
    print(f"Saved {len(counter)} unique words.")