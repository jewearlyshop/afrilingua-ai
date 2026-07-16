from pathlib import Path

from engine.text.normalizer import normalize_text
from engine.text.tokenizer import tokenize

text = Path("engine/corpus/yoruba_sample.txt").read_text(encoding="utf-8")

print(tokenize(normalize_text(text)))