from pathlib import Path

from engine.ai.hybrid_ranker import HybridRanker
from engine.ai.ngram import BigramModel
from engine.language_model.loader import LanguageModel
from engine.language_model.yorubert import YorubaBert
from engine.models import BIGRAM
from engine.text.normalizer import normalize_text
from engine.text.tokenizer import tokenize


MODEL_DIR = "engine/language_model/data_train"
EVALUATION_DIR = Path("corpus/evaluation")


def extract_examples():
    examples = []

    for file in sorted(EVALUATION_DIR.glob("*_eval.txt")):
        for line in file.read_text(encoding="utf-8").splitlines():

            line = line.strip()

            if not line:
                continue

            words = tokenize(normalize_text(line))

            if len(words) < 2:
                continue

            for i in range(1, len(words)):

                expected = words[i]

                if i >= 2:
                    context = (
                        words[i - 2],
                        words[i - 1],
                    )
                else:
                    context = (
                        words[i - 1],
                    )

                examples.append(
                    (context, expected)
                )

    return examples


def load_bigram():
    model = BigramModel()
    model.load(BIGRAM)
    return model


def test_fast_hybrid_language_model_evaluation():

    language_model = LanguageModel(MODEL_DIR)
    bigram = load_bigram()
    yorubert = YorubaBert()
    ranker = HybridRanker()

    examples = extract_examples()

    # Cache statistical predictions and precompute BERT in batches.
    lm_cache = {}
    bigram_cache = {}

    unique_contexts = list(dict.fromkeys(
        " ".join(context) for context, _ in examples
    ))

    bert_cache = {}

    for start in range(0, len(unique_contexts), 4):
        batch = unique_contexts[start:start + 4]
        batch_predictions = yorubert.predict_batch(
            batch,
            limit=5,
            batch_size=4,
        )
        bert_cache.update(zip(batch, batch_predictions))


    totals = {
        1: 0,
        3: 0,
        5: 0,
    }

    predictions = 0
    no_prediction = 0

    for context, expected in examples:

        context_text = " ".join(context)

        # -------------------------
        # Statistical LM
        # -------------------------

        if context not in lm_cache:

            if len(context) >= 2:
                lm_cache[context] = language_model.next_words(
                    context[-2],
                    context[-1],
                )
            else:
                lm_cache[context] = language_model.next_words(
                    context[-1],
                )

        lm_context = lm_cache[context]

        # -------------------------
        # Bigram
        # -------------------------

        previous = context[-1]

        if previous not in bigram_cache:
            bigram_cache[previous] = bigram.predict(previous)

        bigram_context = bigram_cache[previous]

        # -------------------------
        # OYO-BERT (precomputed in batches)
        # -------------------------

        yorubert_context = bert_cache[context_text]

        # -------------------------
        # Hybrid ranking
        # -------------------------

        suggestions = ranker.rank(
            (lm_context, 3),
            (yorubert_context, 2),
            (bigram_context, 2),
        )

        words = [
            item["word"]
            for item in suggestions
        ]

        if not words:
            no_prediction += 1
            continue

        predictions += 1

        if expected in words[:1]:
            totals[1] += 1

        if expected in words[:3]:
            totals[3] += 1

        if expected in words[:5]:
            totals[5] += 1

    total = len(examples)

    print()
    print("Fast Hybrid Language Model Evaluation")
    print("=" * 55)
    print(f"Total examples:    {total}")
    print(f"Predictions made:  {predictions}")
    print(f"No prediction:     {no_prediction}")

    coverage = predictions / total if total else 0

    print(f"Coverage:          {coverage:.1%}")

    print()

    for k in (1, 3, 5):
        rate = totals[k] / total if total else 0

        print(
            f"Top-{k}: {totals[k]} "
            f"({rate:.1%})"
        )

    print()
    print(f"Unique LM contexts:     {len(lm_cache)}")
    print(f"Unique Bigram contexts: {len(bigram_cache)}")
    print(f"Unique BERT contexts:   {len(bert_cache)}")

    assert total > 0