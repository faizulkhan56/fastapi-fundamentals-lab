from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """
    Pydantic model representing an item in our API.

    Fields:
    - id: unique integer identifier
    - name: short name of the item
    - description: optional text describing the item
    """
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class Features(BaseModel):
    """
    Pydantic model for ML prediction input features.
    
    Fields:
    - feature1: First feature value (float)
    - feature2: Second feature value (float)
    - feature3: Third feature value (float)
    """
    feature1: float
    feature2: float
    feature3: float

    class Config:
        json_schema_extra = {
            "example": {
                "feature1": 1.5,
                "feature2": 2.3,
                "feature3": 0.8
            }
        }


class PredictionResponse(BaseModel):
    """
    Pydantic model for ML prediction response.
    
    Fields:
    - prediction: The predicted value (float)
    """
    prediction: float

    class Config:
        json_schema_extra = {
            "example": {
                "prediction": 5.23
            }
        }
