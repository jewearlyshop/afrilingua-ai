from backend.services.context_service import get_bigram

model = get_bigram()

print("Known words:")
print(list(model.model.keys()))

print("\nPredictions for 'fẹ́':")
print(model.predict("fẹ́"))

print("\nPredictions for 'fẹ':")
print(model.predict("fẹ"))