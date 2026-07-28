from engine.spellcheck.spell_checker import spell_suggestions

from collections import Counter

vocabulary = Counter({
    "ọmọ": 10,
    "ọmọkùnrin": 3,
    "ọmọbìnrin": 2,
    "ọba": 1,
})

print(spell_suggestions("ọmo", vocabulary))