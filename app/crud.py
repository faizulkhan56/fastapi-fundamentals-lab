from typing import List, Optional
from .models import Item
from .database import items_db


def get_items() -> List[Item]:
    return items_db


def get_item(item_id: int) -> Optional[Item]:
    for item in items_db:
        if item.id == item_id:
            return item
    return None


def create_item(item: Item) -> Item:
    items_db.append(item)
    return item


def update_item(item_id: int, updated_item: Item) -> Optional[Item]:
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    return None


def delete_item(item_id: int) -> bool:
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return True
    return False
