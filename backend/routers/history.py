from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.history_service import get_history


router = APIRouter(prefix="/history", tags=["Learning"])


class Selection(BaseModel):
    previous: str
    selected: str


@router.post("/")
def learn(selection: Selection):
    history = get_history()

    history.record(
        selection.previous,
        selection.selected
    )

    return {"status": "learned"}