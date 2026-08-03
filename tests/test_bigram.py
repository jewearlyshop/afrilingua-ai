from engine.ai.ngram import BigramModel

text = """
Mo fẹ́ lọ.
Mo fẹ́ jẹun.
Mo fẹ́ lọ.
Mo fẹ́ kọ́.
"""

model = BigramModel()

model.train(text)

print(model.predict("fẹ́"))