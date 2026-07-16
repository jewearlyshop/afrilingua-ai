from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.predict import router as predict_router
from backend.routers.history import router as history_router

app = FastAPI(
    title="AfriLingua AI",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router)
app.include_router(history_router)


@app.get("/")
def home():
    return {
        "project": "AfriLingua AI",
        "status": "running",
    }