from engine.ai.hybrid_ranker import HybridRanker

ranker = HybridRanker()

trie = [
    "lọ",
    "lọwọ"
]

bigram = [
    "lọ",
    "jẹun",
    "kọ́"
]

history = [
    "lọ"
]

print(
    ranker.rank(
        trie,
        bigram,
        history
    )
)