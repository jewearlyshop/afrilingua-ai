from collections import Counter


class RankingEngine:
    def __init__(self, vocabulary: Counter):
        self.vocabulary = vocabulary

    def rank(self, words):
        """
        Rank words by frequency (highest first).
        """
        return sorted(
            words,
            key=lambda word: self.vocabulary.get(word, 0),
            reverse=True,
        )