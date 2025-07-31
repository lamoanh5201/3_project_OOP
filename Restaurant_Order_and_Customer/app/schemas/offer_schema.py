from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

class OfferBase(BaseModel):
    name: str
    description: Optional[str] = None
    discount_percentage: Decimal
    start_date: datetime
    end_date: datetime
    is_active: bool = True

class OfferCreate(OfferBase):
    pass

class OfferUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    discount_percentage: Optional[Decimal] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class OfferResponse(OfferBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True