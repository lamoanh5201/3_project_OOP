from sqlmodel import Field
from typing import Optional
from .base import Base

class Customer(Base, table=True):
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    phone: Optional[str] = None
    address: Optional[str] = None