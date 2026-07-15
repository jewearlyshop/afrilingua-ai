from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.predict import router

app = FastAPI(
    title="AfriLingua AI",
    version="0.1.0"
)

# Allow the React frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(router)


@app.get("/")
def home():
    return {
        "project": "AfriLingua AI",
        "status": "running"
    }