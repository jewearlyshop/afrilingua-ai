from engine.language_model.yorubert import YorubaBert


def test_yorubert_returns_words():
    model = YorubaBert()

    results = model.predict("lọ sí")

    assert len(results) > 0
    assert all(isinstance(word, str) for word in results)


def test_yorubert_uses_yoruba_vocabulary():
    model = YorubaBert()

    results = model.predict("ọmọ náà fẹ́")

    assert len(results) > 0
    assert all(word in model.vocabulary for word in results)


def test_yorubert_limit():
    model = YorubaBert()

    results = model.predict("lọ sí", limit=3)

    assert len(results) <= 3


def test_yorubert_repeated_context_returns_same_predictions():
    model = YorubaBert()

    context = "ọmọ náà fẹ́"

    first = model.predict(context, limit=5)
    second = model.predict(context, limit=5)

    assert first == second
    assert len(first) <= 5
    assert all(word in model.vocabulary for word in first)