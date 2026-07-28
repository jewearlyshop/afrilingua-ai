def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)

    if len(b) == 0:
        return len(a)

    previous = list(range(len(b) + 1))

    for i, c1 in enumerate(a):
        current = [i + 1]

        for j, c2 in enumerate(b):
            insertions = previous[j + 1] + 1
            deletions = current[j] + 1
            substitutions = previous[j] + (c1 != c2)

            current.append(
                min(insertions, deletions, substitutions)
            )

        previous = current

    return previous[-1]


from engine.text.tone_normalizer import strip_diacritics


def spell_suggestions(word, vocabulary, limit=5):
    normalized_word = strip_diacritics(word)

    candidates = []

    for candidate, frequency in vocabulary.items():
        normalized_candidate = strip_diacritics(candidate)

        distance = levenshtein(
            normalized_word,
            normalized_candidate
        )

        score = -distance

        if normalized_candidate.startswith(normalized_word):
            score += 5

        score += frequency

        candidates.append(
            (score, candidate)
        )

    candidates.sort(reverse=True)

    return [
        candidate
        for score, candidate in candidates[:limit]
    ]