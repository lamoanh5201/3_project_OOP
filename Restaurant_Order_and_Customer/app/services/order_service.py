from sqlmodel import Session, select
from typing import List, Optional
from app.models.order_model import Order
from app.schemas.order_schema import OrderCreate, OrderUpdate

class OrderService:
    def __init__(self, session: Session):
        self.session = session

    def create_order(self, order_data: OrderCreate) -> Order:
        order = Order(**order_data.dict())
        self.session.add(order)
        self.session.commit()
        self.session.refresh(order)
        return order

    def get_order(self, order_id: int) -> Optional[Order]:
        return self.session.get(Order, order_id)

    def get_orders(self, skip: int = 0, limit: int = 100) -> List[Order]:
        statement = select(Order).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def get_orders_by_customer(self, customer_id: int) -> List[Order]:
        statement = select(Order).where(Order.customer_id == customer_id)
        return self.session.exec(statement).all()

    def update_order(self, order_id: int, order_data: OrderUpdate) -> Optional[Order]:
        order = self.session.get(Order, order_id)
        if order:
            for key, value in order_data.dict(exclude_unset=True).items():
                setattr(order, key, value)
            self.session.commit()
            self.session.refresh(order)
        return order

    def delete_order(self, order_id: int) -> bool:
        order = self.session.get(Order, order_id)
        if order:
            self.session.delete(order)
            self.session.commit()
            return True
        return False