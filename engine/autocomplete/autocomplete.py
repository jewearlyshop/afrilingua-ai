from engine.autocomplete.trie import Trie


class AutocompleteEngine:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.trie = Trie()

        for word in vocabulary:
            self.trie.insert(word)

    def suggest(self, prefix, limit=5):
        matches = self.trie.autocomplete(prefix)

        matches.sort(
            key=lambda word: self.vocabulary[word],
            reverse=True
        )

        return matches[:limit]