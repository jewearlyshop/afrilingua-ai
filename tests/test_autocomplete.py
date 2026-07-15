from engine.autocomplete.autocomplete import AutocompleteEngine

vocabulary = {
    "ọmọ": 100,
    "ọmọde": 40,
    "ọmọkùnrin": 25,
    "ọmọbìnrin": 15,
    "ọba": 60,
    "ilé": 30
}

engine = AutocompleteEngine(vocabulary)

print(engine.suggest("ọm"))