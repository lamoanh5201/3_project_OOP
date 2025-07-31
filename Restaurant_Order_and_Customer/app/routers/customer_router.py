from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.services.customer_service import CustomerService
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate, CustomerResponse

router = APIRouter()

@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, session: Session = Depends(get_session)):
    service = CustomerService(session)
    return service.create_customer(customer)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, session: Session = Depends(get_session)):
    service = CustomerService(session)
    customer = service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/", response_model=List[CustomerResponse])
def get_customers(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    service = CustomerService(session)
    return service.get_customers(skip=skip, limit=limit)

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: CustomerUpdate, session: Session = Depends(get_session)):
    service = CustomerService(session)
    updated_customer = service.update_customer(customer_id, customer)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, session: Session = Depends(get_session)):
    service = CustomerService(session)
    if not service.delete_customer(customer_id):
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}