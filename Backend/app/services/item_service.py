from sqlalchemy.orm import Session
from app.schemas.item import ItemCreate
from app.repositories.item_repository import create_item, get_items

def create_item_service(db: Session, item: ItemCreate):
    return create_item(db, item)

def get_items_service(db: Session):
    return get_items(db)
