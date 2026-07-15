from engine.ai.ngram import BigramModel

words = [
    "Mo", "fẹ́", "lọ",
    "Mo", "fẹ́", "jẹun",
    "Mo", "fẹ́", "lọ",
    "Mo", "fẹ́", "kọ́",
]

model = BigramModel()

model.train(words)

print(model.predict("fẹ́"))