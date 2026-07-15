import re

WORD_PATTERN = re.compile(r"[^\W\d_]+", re.UNICODE)

def tokenize(text):
    return WORD_PATTERN.findall(text)