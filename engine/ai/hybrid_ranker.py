from collections import Counter


class HybridRanker:

    def rank(self, *sources, limit=5):
        scores = Counter()

        for source in sources:

            # Default weight
            weight = 1

            # Allow (suggestions, weight)
            if isinstance(source, tuple):
                suggestions, weight = source
            else:
                suggestions = source

            for index, word in enumerate(suggestions):
                scores[word] += (len(suggestions) - index) * weight

        ranked = scores.most_common(limit)

        return [
            {
                "word": word,
                "score": score,
            }
            for word, score in ranked
        ]