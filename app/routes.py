from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .models import Item, Features, PredictionResponse
from . import crud
from .model_loader import get_model, predict as make_prediction

router = APIRouter()


@router.get("/items/", response_model=List[Item])
async def read_items():
    return crud.get_items()


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    return crud.create_item(item)


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    item = crud.update_item(item_id, updated_item)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    success = crud.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}


@router.get("/filter/")
async def filter_items(category: str, price_lt: float):
    return {
        "category": category,
        "price_less_than": price_lt,
    }


@router.get("/search/")
async def search_items(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    results = {"items": [{"item_id": "123"}, {"item_id": "456"}]}
    if q:
        results.update({"q": q})
    return results


@router.post("/predict/", response_model=PredictionResponse)
async def predict(features: Features):
    """
    ML Prediction Endpoint
    
    Accepts feature values and returns a prediction using the trained ML model.
    
    Args:
        features: Features object containing feature1, feature2, and feature3
    
    Returns:
        PredictionResponse with the predicted value
    
    Raises:
        HTTPException: If model is not loaded or prediction fails
    """
    try:
        model = get_model()
        if model is None:
            raise HTTPException(
                status_code=503,
                detail="ML model is not available. Please ensure the model is loaded."
            )
        
        # Extract features as list
        feature_list = [features.feature1, features.feature2, features.feature3]
        
        # Make prediction
        prediction_value = make_prediction(feature_list)
        
        return PredictionResponse(prediction=prediction_value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
