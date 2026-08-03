from engine.language_model.loader import LanguageModel

lm = LanguageModel()

print("Bigram:")
print(lm.next_words("lọ"))

print()

print("Trigram:")
print(lm.next_words("lọ", "sí"))