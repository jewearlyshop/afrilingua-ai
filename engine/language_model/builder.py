from collections import Counter
from pathlib import Path
import json

from engine.text.tokenizer import tokenize


def build_language_model(corpus_dir, output_dir):
    corpus = Path(corpus_dir)

    unigram = Counter()
    bigram = Counter()
    trigram = Counter()

    for file in corpus.rglob("*.txt"):
        with file.open("r", encoding="utf-8") as f:
            words = tokenize(f.read())

        unigram.update(words)

        for i in range(len(words) - 1):
            bigram[(words[i], words[i + 1])] += 1

        for i in range(len(words) - 2):
            trigram[(words[i], words[i + 1], words[i + 2])] += 1

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    with open(output / "vocabulary.json", "w", encoding="utf-8") as f:
        json.dump(unigram, f, ensure_ascii=False, indent=4)

    with open(output / "bigrams.json", "w", encoding="utf-8") as f:
        json.dump(
            {" ".join(k): v for k, v in bigram.items()},
            f,
            ensure_ascii=False,
            indent=4,
        )

    with open(output / "trigrams.json", "w", encoding="utf-8") as f:
        json.dump(
            {" ".join(k): v for k, v in trigram.items()},
            f,
            ensure_ascii=False,
            indent=4,
        )

    print("Vocabulary:", len(unigram))
    print("Bigrams:", len(bigram))
    print("Trigrams:", len(trigram))