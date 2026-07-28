from collections import Counter


class HybridRanker:

    def rank(self, *lists, limit=5):
        scores = Counter()

        for suggestions in lists:
            for index, word in enumerate(suggestions):
                scores[word] += len(suggestions) - index

        ranked = scores.most_common(limit)

        return [
            {
                "word": word,
                "score": score,
            }
            for word, score in ranked
        ]