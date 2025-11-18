from fastapi import FastAPI
from .routes import router as api_router

app = FastAPI(
    title="FastAPI Fundamentals Lab",
    description="Lab project to learn FastAPI basics, CRUD, and API design.",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Fundamentals Lab API"}


app.include_router(api_router)
