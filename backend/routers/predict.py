from fastapi import APIRouter
from backend.services.prediction_pipeline import PredictionPipeline

router = APIRouter(prefix="/predict", tags=["Prediction"])

pipeline = PredictionPipeline()


@router.get("/{prefix}")
def predict(prefix: str):
    return {
        "typed": prefix,
        "suggestions": pipeline.predict(prefix)
    }