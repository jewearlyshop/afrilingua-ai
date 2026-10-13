from pathlib import Path

import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

from engine.vocabulary.loader import load_vocabulary


class YorubaBert:
    """Yoruba masked-language model with vocabulary-aware predictions."""

    MODEL_NAME = "Davlan/oyo-bert-base"

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, vocabulary_path=None):
        if getattr(self, "_initialized", False):
            return

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.MODEL_NAME
        )

        self.model = AutoModelForMaskedLM.from_pretrained(
            self.MODEL_NAME
        )

        self.model.eval()

        if vocabulary_path is None:
            vocabulary_path = (
                Path(__file__).parents[1]
                / "vocabulary"
                / "vocabulary.json"
            )

        self.vocabulary = load_vocabulary(vocabulary_path)

        self.word_token_ids = {}

        for word in self.vocabulary:
            tokens = self.tokenizer.tokenize(word)

            if len(tokens) != 1:
                continue

            token_id = self.tokenizer.convert_tokens_to_ids(tokens[0])

            if token_id != self.tokenizer.unk_token_id:
                self.word_token_ids[word] = token_id

        self._candidate_words = list(self.word_token_ids.keys())
        self._candidate_token_ids = torch.tensor(
            list(self.word_token_ids.values()),
            dtype=torch.long,
        )

        self._cache = {}

        self._initialized = True

    def predict(self, text, limit=5):
        """Return vocabulary words most likely in the masked position."""

        text = text.strip()

        if not text:
            return []

        cache_key = (text, limit)

        if cache_key in self._cache:
            return self._cache[cache_key]

        masked_text = text + " " + self.tokenizer.mask_token

        inputs = self.tokenizer(
            masked_text,
            return_tensors="pt"
        )

        mask_positions = (
            inputs["input_ids"][0]
            == self.tokenizer.mask_token_id
        )

        if not mask_positions.any():
            return []

        mask_index = mask_positions.nonzero(
            as_tuple=True
        )[0][0]

        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits[0, mask_index]

        words = self._candidate_words
        scores = logits[self._candidate_token_ids]


        top_k = min(limit, len(scores))

        top_scores, top_indices = torch.topk(
            scores,
            k=top_k
        )

        results = [
            words[index]
            for index in top_indices.tolist()
        ]
        self._cache[cache_key] = results

        return results

    def predict_batch(self, texts, limit=5, batch_size=8):
        """Predict vocabulary words for multiple contexts in batches."""

        if batch_size < 1:
            raise ValueError("batch_size must be at least 1")

        if limit < 1:
            raise ValueError("limit must be at least 1")

        results = [None] * len(texts)
        pending_texts = []
        pending_indices = []

        for index, text in enumerate(texts):
            text = text.strip()

            if not text:
                results[index] = []
                continue

            cache_key = (text, limit)

            if cache_key in self._cache:
                results[index] = self._cache[cache_key]
            else:
                pending_texts.append(text)
                pending_indices.append(index)

        words = self._candidate_words
        token_ids = self._candidate_token_ids
        top_k = min(limit, len(words))

        for start in range(0, len(pending_texts), batch_size):
            batch_texts = pending_texts[start:start + batch_size]
            batch_indices = pending_indices[start:start + batch_size]

            masked_texts = [
                text + " " + self.tokenizer.mask_token
                for text in batch_texts
            ]

            inputs = self.tokenizer(
                masked_texts,
                return_tensors="pt",
                padding=True,
                truncation=True,
            )

            mask_positions = (
                inputs["input_ids"] == self.tokenizer.mask_token_id
            )

            with torch.no_grad():
                outputs = self.model(**inputs)

            for row, (text, original_index) in enumerate(
                zip(batch_texts, batch_indices)
            ):
                positions = mask_positions[row].nonzero(
                    as_tuple=True
                )[0]

                if len(positions) == 0:
                    prediction = []
                else:
                    logits = outputs.logits[row, positions[0]]
                    scores = logits[token_ids]

                    top_indices = torch.topk(
                        scores,
                        k=top_k,
                    ).indices.tolist()

                    prediction = [words[i] for i in top_indices]

                self._cache[(text, limit)] = prediction
                results[original_index] = prediction

        return results
