from sqlmodel import Field
from typing import Optional
from decimal import Decimal
from enum import Enum
from .base import Base

class PaymentMethod(str, Enum):
    CASH = "cash"
    CARD = "card"
    ONLINE = "online"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class Payment(Base, table=True):
    order_id: int = Field(foreign_key="order.id")
    amount: Decimal = Field(decimal_places=2)
    method: PaymentMethod
    status: PaymentStatus = Field(default=PaymentStatus.PENDING)
    transaction_id: Optional[str] = None