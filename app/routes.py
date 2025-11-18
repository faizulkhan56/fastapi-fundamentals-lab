from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .models import Item
from . import crud

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
