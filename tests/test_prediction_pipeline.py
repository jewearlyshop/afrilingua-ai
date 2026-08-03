from backend.services.prediction_pipeline import PredictionPipeline

pipeline = PredictionPipeline()


def test_prefix_autocomplete():
    results = pipeline.predict("ọm")
    assert len(results) > 0
    assert results[0]["word"] == "ọmọ"


def test_tone_restoration():
    results = pipeline.predict("omo")
    assert len(results) > 0
    assert results[0]["word"] == "ọmọ"


def test_context_prediction():
    results = pipeline.predict("lọ sí")
    assert len(results) > 0