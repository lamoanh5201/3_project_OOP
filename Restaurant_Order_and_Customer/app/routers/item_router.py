from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.services.item_service import ItemService
from app.schemas.item_schema import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, session: Session = Depends(get_session)):
    service = ItemService(session)
    return service.create_item(item)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, session: Session = Depends(get_session)):
    service = ItemService(session)
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/", response_model=List[ItemResponse])
def get_items(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    service = ItemService(session)
    return service.get_items(skip=skip, limit=limit)

@router.get("/category/{category}", response_model=List[ItemResponse])
def get_items_by_category(category: str, session: Session = Depends(get_session)):
    service = ItemService(session)
    return service.get_items_by_category(category)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, session: Session = Depends(get_session)):
    service = ItemService(session)
    updated_item = service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    service = ItemService(session)
    if not service.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}