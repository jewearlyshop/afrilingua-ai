from fastapi import APIRouter

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

@router.get("/{prefix}")
def predict(prefix: str):
    return {
        "typed": prefix,
        "suggestions": [
            "ọmọ",
            "ọmọde",
            "ọmọkùnrin",
            "ọmọbìnrin"
        ]
    }