from engine.tone.tone_restorer import ToneRestorer

vocabulary = [
    "ọmọ",
    "ọmọkùnrin",
    "ọmọbìnrin",
    "ilé",
    "ìwé",
    "fẹ́",
    "lọ",
    "ọba",
]

restorer = ToneRestorer(vocabulary)

print(restorer.restore_word("omo"))
print(restorer.restore_word("ile"))
print(restorer.restore_word("iwe"))

print(restorer.restore_sentence("omo fe lo ile"))