from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.services.order_service import OrderService
from app.schemas.order_schema import OrderCreate, OrderUpdate, OrderResponse

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    service = OrderService(session)
    return service.create_order(order)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, session: Session = Depends(get_session)):
    service = OrderService(session)
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/", response_model=List[OrderResponse])
def get_orders(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    service = OrderService(session)
    return service.get_orders(skip=skip, limit=limit)

@router.get("/customer/{customer_id}", response_model=List[OrderResponse])
def get_orders_by_customer(customer_id: int, session: Session = Depends(get_session)):
    service = OrderService(session)
    return service.get_orders_by_customer(customer_id)

@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderUpdate, session: Session = Depends(get_session)):
    service = OrderService(session)
    updated_order = service.update_order(order_id, order)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}")
def delete_order(order_id: int, session: Session = Depends(get_session)):
    service = OrderService(session)
    if not service.delete_order(order_id):
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}