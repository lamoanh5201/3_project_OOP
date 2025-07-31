from sqlmodel import Field, Relationship
from typing import Optional
from decimal import Decimal
from enum import Enum
from .base import Base

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order(Base, table=True):
    customer_id: int = Field(foreign_key="customer.id")
    total_amount: Decimal = Field(decimal_places=2)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    notes: Optional[str] = None