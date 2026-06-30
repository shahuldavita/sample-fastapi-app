from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    description: str = ""

_db: List[Item] = []

@router.get("/", response_model=List[Item])
def list_items():
    return _db

@router.post("/", response_model=Item, status_code=201)
def create_item(item: Item):
    _db.append(item)
    return item

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
