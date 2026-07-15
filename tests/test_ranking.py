from collections import Counter

from engine.autocomplete.ranking import RankingEngine

vocabulary = Counter({
    "ọmọ": 120,
    "ọmọde": 75,
    "ọmọkùnrin": 30,
    "ọmọbìnrin": 20,
})

engine = RankingEngine(vocabulary)

words = [
    "ọmọbìnrin",
    "ọmọ",
    "ọmọkùnrin",
    "ọmọde",
]

print(engine.rank(words))