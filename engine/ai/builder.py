from engine.ai.ngram import BigramModel
from engine.text.corpus_loader import load_corpus


def build_bigram_model(output_file):
    text = load_corpus()

    model = BigramModel()
    model.train(text)
    model.save(output_file)

    print("Bigram model built.")