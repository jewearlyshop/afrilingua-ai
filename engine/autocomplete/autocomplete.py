from engine.autocomplete.trie import Trie
from engine.autocomplete.ranking import RankingEngine


class AutocompleteEngine:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.trie = Trie()
        self.ranker = RankingEngine(vocabulary)

        for word in vocabulary:
            self.trie.insert(word)

    def suggest(self, prefix, limit=5):
        matches = self.trie.autocomplete(prefix)
        ranked = self.ranker.rank(matches)
        return ranked[:limit]