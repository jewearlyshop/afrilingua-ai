from fastapi import APIRouter
from services.prediction_service import get_engine

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.get("/{prefix}")
def predict(prefix: str):
    engine = get_engine()

    return {
        "typed": prefix,
        "suggestions": engine.suggest(prefix)
    }