from sqlmodel import Session, select
from typing import List, Optional
from app.models.item_model import Item
from app.schemas.item_schema import ItemCreate, ItemUpdate

class ItemService:
    def __init__(self, session: Session):
        self.session = session

    def create_item(self, item_data: ItemCreate) -> Item:
        item = Item(**item_data.dict())
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def get_item(self, item_id: int) -> Optional[Item]:
        return self.session.get(Item, item_id)

    def get_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        statement = select(Item).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def get_items_by_category(self, category: str) -> List[Item]:
        statement = select(Item).where(Item.category == category)
        return self.session.exec(statement).all()

    def update_item(self, item_id: int, item_data: ItemUpdate) -> Optional[Item]:
        item = self.session.get(Item, item_id)
        if item:
            for key, value in item_data.dict(exclude_unset=True).items():
                setattr(item, key, value)
            self.session.commit()
            self.session.refresh(item)
        return item

    def delete_item(self, item_id: int) -> bool:
        item = self.session.get(Item, item_id)
        if item:
            self.session.delete(item)
            self.session.commit()
            return True
        return False