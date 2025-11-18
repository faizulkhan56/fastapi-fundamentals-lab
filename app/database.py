from typing import List
from .models import Item

# This module simulates a database using an in-memory Python list.

items_db: List[Item] = [
    Item(id=1, name="Item One", description="This is the first item."),
    Item(id=2, name="Item Two", description="This is the second item."),
    Item(id=3, name="Item Three", description="This is the third item."),
]
