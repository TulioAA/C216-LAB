from fastapi import APIRouter
from app.schemas.item import ItemCreate, ItemUpdate

router = APIRouter()

# "Banco" em memória
items = {}

# Endpoints de status
@router.get("/")
def read_root():
    return {"message": "Backend funcionando"}

@router.get("/health")
def health_check():
    return {"status": "ok"}

# CRUD
@router.get("/items")
def list_items():
    return list(items.values())

@router.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

@router.post("/items")
def create_item(item: ItemCreate):
    new_id = len(items) + 1
    items[new_id] = {"id": new_id, **item.model_dump()}
    return items[new_id]

@router.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    items[item_id] = {"id": item_id, **item.model_dump()}
    return items[item_id]

@router.patch("/items/{item_id}")
def patch_item(item_id: int, item: ItemUpdate):
    if item_id in items:
        items[item_id].update(item.model_dump(exclude_unset=True))
        return items[item_id]
    return {"error": "Item not found"}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return items.pop(item_id, {"error": "Item not found"})

# Query Parameters
@router.get("/items/search")
def search_items(name: str):
    return [item for item in items.values() if item["name"] == name]
