from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from .routes import router as api_router
from .model_loader import load_model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events.
    Loads ML model at startup and performs cleanup at shutdown.
    """
    # Startup: Load ML model
    logger.info("Starting up FastAPI application...")
    model_path = "models/model.pkl"
    model = load_model(model_path)
    if model is not None:
        logger.info("ML model loaded successfully")
    else:
        logger.warning("ML model could not be loaded. Predict endpoint may not work.")
    
    yield
    
    # Shutdown: Cleanup (if needed)
    logger.info("Shutting down FastAPI application...")


app = FastAPI(
    title="FastAPI Fundamentals Lab",
    description="Lab project to learn FastAPI basics, CRUD, API design, and ML model deployment.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the FastAPI Fundamentals Lab API",
        "endpoints": {
            "docs": "/docs",
            "items": "/items/",
            "predict": "/predict/"
        }
    }


app.include_router(api_router)
