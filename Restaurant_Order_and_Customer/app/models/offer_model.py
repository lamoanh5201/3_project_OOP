from sqlmodel import Field
from typing import Optional
from decimal import Decimal
from datetime import datetime
from .base import Base

class Offer(Base, table=True):
    name: str = Field(index=True)
    description: Optional[str] = None
    discount_percentage: Decimal = Field(decimal_places=2)
    start_date: datetime
    end_date: datetime
    is_active: bool = Field(default=True)