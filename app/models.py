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
