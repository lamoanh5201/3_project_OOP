from sqlmodel import Field
from typing import Optional
from decimal import Decimal
from .base import Base

class Item(Base, table=True):
    name: str = Field(index=True)
    description: Optional[str] = None
    price: Decimal = Field(decimal_places=2)
    category: str = Field(index=True)
    is_available: bool = Field(default=True)