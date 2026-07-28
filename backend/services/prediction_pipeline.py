from backend.services.prediction_service import get_engine
from backend.services.context_service import get_bigram
from backend.services.history_service import get_history

from engine.ai.hybrid_ranker import HybridRanker
from engine.text.normalizer import normalize_text
from engine.spellcheck.spell_checker import spell_suggestions


class PredictionPipeline:
    def __init__(self):
        self.engine = get_engine()
        self.bigram = get_bigram()
        self.history = get_history()
        self.ranker = HybridRanker()

    def predict(self, text: str):
        original = text

        text = text.lstrip()

        if not text:
            return []

        words = text.split()

        # User has just finished a word
        if original.endswith(" "):
            previous = normalize_text(words[-1])

            bigram = self.bigram.predict(previous)
            history = self.history.predict(previous)

            return self.ranker.rank(
                bigram,
                history
            )

        # First word only
        if len(words) == 1:
            current = normalize_text(words[0])

            trie = self.engine.suggest(current)

            if not trie:
                trie = spell_suggestions(
                    current,
                    self.engine.vocabulary
                )

            return self.ranker.rank(trie)

        # User is typing after another word
        previous = normalize_text(words[-2])
        current = normalize_text(words[-1])

        trie = self.engine.suggest(current)

        if not trie:
            trie = spell_suggestions(
                current,
                self.engine.vocabulary
            )

        context = [
            word
            for word in self.bigram.predict(previous)
            if word.startswith(current)
        ]

        history = [
            word
            for word in self.history.predict(previous)
            if word.startswith(current)
        ]

        return self.ranker.rank(
            trie,
            context,
            history
        )