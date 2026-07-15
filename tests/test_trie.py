from engine.autocomplete.trie import Trie

trie = Trie()

words = [
    "ọmọ",
    "ọmọde",
    "ọmọbìnrin",
    "ọmọkùnrin",
    "ọba",
    "ilé",
]

for word in words:
    trie.insert(word)

print(trie.autocomplete("ọm"))