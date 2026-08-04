from backend.services.prediction_service import get_engine
from backend.services.context_service import get_bigram
from backend.services.history_service import get_history

from engine.ai.hybrid_ranker import HybridRanker
from engine.text.normalizer import normalize_text
from engine.spellcheck.spell_checker import spell_suggestions
from engine.tone.tone_restorer import ToneRestorer
from engine.language_model.loader import LanguageModel
from engine.user_learning.learner import UserLearner



class PredictionPipeline:
    def __init__(self):
        self.engine = get_engine()
        self.bigram = get_bigram()
        self.history = get_history()
        self.ranker = HybridRanker()
        self.tone_restorer = ToneRestorer()
        self.language_model = LanguageModel()
        self.user_learner = UserLearner()

    def predict(self, text: str):

        original = text
        text = normalize_text(text)
        words = text.split()

        if len(words) >= 2:
            lm_context = self.language_model.next_words(
                words[-2],
                words[-1]
            )

        elif len(words) == 1:
            lm_context = self.language_model.next_words(
                words[-1]
            )

        else:
            lm_context = []  

        # Continue with trie, spell check, history, etc.

        text = text.lstrip()

        if not text:
            return []


        # User has just finished a word
        if original.endswith(" "):
            previous = normalize_text(words[-1])

            bigram = self.bigram.predict(previous)
            history = self.history.predict(previous)

            suggestions = self.ranker.rank(
                bigram,
                lm_context,
                history
            )
        
            for item in suggestions:
                item["word"] = self.tone_restorer.restore_word(
                    item["word"]
                )
            
            return suggestions

        # First word only
        if len(words) == 1:
            current = normalize_text(words[0])

            trie = self.engine.suggest(current)

            spell = []

            if not trie:
                spell = spell_suggestions(
                    current,
                    self.engine.vocabulary
                )

            suggestions = self.ranker.rank(
                (trie, 2),
                (spell, 1),
                )

            for item in suggestions:
                item["word"] = self.tone_restorer.restore_word(
                    item["word"]
                )
            return suggestions

        # User is typing after another word
        previous = normalize_text(words[-2])
        current = normalize_text(words[-1])

        trie = self.engine.suggest(current)

        spell = []

        if not trie:
            spell = spell_suggestions(
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

        user = self.user_learner.predict(current)

        suggestions = self.ranker.rank(
            (user, 5),  # User history
            (history, 4),  # System history
            (lm_context, 3),  # Language model context
            (context, 2),  # Contextual suggestions
            (trie, 1),
            (spell, 1),  # Spell check suggestions
        )
        
        for item in suggestions:
            item["word"] = self.tone_restorer.restore_word(
                item["word"]
            )
        
        return suggestions