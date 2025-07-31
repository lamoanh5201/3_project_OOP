from sqlmodel import Session, select
from typing import List, Optional
from app.models.customer_model import Customer
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate

class CustomerService:
    def __init__(self, session: Session):
        self.session = session

    def create_customer(self, customer_data: CustomerCreate) -> Customer:
        customer = Customer(**customer_data.dict())
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        return self.session.get(Customer, customer_id)

    def get_customers(self, skip: int = 0, limit: int = 100) -> List[Customer]:
        statement = select(Customer).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def update_customer(self, customer_id: int, customer_data: CustomerUpdate) -> Optional[Customer]:
        customer = self.session.get(Customer, customer_id)
        if customer:
            for key, value in customer_data.dict(exclude_unset=True).items():
                setattr(customer, key, value)
            self.session.commit()
            self.session.refresh(customer)
        return customer

    def delete_customer(self, customer_id: int) -> bool:
        customer = self.session.get(Customer, customer_id)
        if customer:
            self.session.delete(customer)
            self.session.commit()
            return True
        return False