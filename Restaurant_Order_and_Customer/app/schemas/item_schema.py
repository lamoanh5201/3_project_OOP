from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    category: str
    is_available: bool = True

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    category: Optional[str] = None
    is_available: Optional[bool] = None

class ItemResponse(ItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True