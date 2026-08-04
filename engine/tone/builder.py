import json
from pathlib import Path

from engine.tone.tone_map import build_tone_map


def build_tone_dictionary(vocabulary_file, output_file):
    with open(vocabulary_file, encoding="utf-8") as f:
        vocabulary = json.load(f)

    # vocabulary.json is a dict of word -> frequency
    words = vocabulary.keys()

    tone_map = build_tone_map(words)

    output = Path(output_file)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8") as f:
        json.dump(tone_map, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(tone_map)} tone entries.")