from engine.ai.ngram import BigramModel

model = BigramModel()

model.train(
    "Mo fẹ́ lọ sí ilé. Mo fẹ́ jẹun."
)

model.save("bigram.json")

loaded = BigramModel()
loaded.load("bigram.json")

print(
    loaded.predict("fẹ́")
)