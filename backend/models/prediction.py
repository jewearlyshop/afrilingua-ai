from pydantic import BaseModel


class Suggestion(BaseModel):
    word: str
    score: int


class PredictionResponse(BaseModel):
    typed: str
    suggestions: list[Suggestion]