from backend.services.prediction_pipeline import PredictionPipeline

pipeline = PredictionPipeline()

print(pipeline.predict("ọm"))
print(pipeline.predict("Mo fẹ́ "))
print(pipeline.predict("Mo fẹ́ l"))