from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.item import ItemCreate, Item
from app.services.item_service import create_item_service, get_items_service

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item_service(db, item)

@router.get("/", response_model=list[Item])
def list_items(db: Session = Depends(get_db)):
    return get_items_service(db)
