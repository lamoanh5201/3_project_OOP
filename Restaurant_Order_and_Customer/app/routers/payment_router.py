from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.services.payment_service import PaymentService
from app.schemas.payment_schema import PaymentCreate, PaymentUpdate, PaymentResponse
from app.models.payment_model import PaymentStatus

router = APIRouter()

@router.post("/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, session: Session = Depends(get_session)):
    service = PaymentService(session)
    return service.create_payment(payment)

@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: int, session: Session = Depends(get_session)):
    service = PaymentService(session)
    payment = service.get_payment(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.get("/", response_model=List[PaymentResponse])
def get_payments(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    service = PaymentService(session)
    return service.get_payments(skip=skip, limit=limit)

@router.get("/order/{order_id}", response_model=List[PaymentResponse])
def get_payments_by_order(order_id: int, session: Session = Depends(get_session)):
    service = PaymentService(session)
    return service.get_payments_by_order(order_id)

@router.get("/status/{status}", response_model=List[PaymentResponse])
def get_payments_by_status(status: PaymentStatus, session: Session = Depends(get_session)):
    service = PaymentService(session)
    return service.get_payments_by_status(status)

@router.put("/{payment_id}", response_model=PaymentResponse)
def update_payment(payment_id: int, payment: PaymentUpdate, session: Session = Depends(get_session)):
    service = PaymentService(session)
    updated_payment = service.update_payment(payment_id, payment)
    if not updated_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated_payment

@router.patch("/{payment_id}/complete", response_model=PaymentResponse)
def complete_payment(payment_id: int, transaction_id: str = None, session: Session = Depends(get_session)):
    service = PaymentService(session)
    completed_payment = service.complete_payment(payment_id, transaction_id)
    if not completed_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return completed_payment

@router.patch("/{payment_id}/fail", response_model=PaymentResponse)
def fail_payment(payment_id: int, session: Session = Depends(get_session)):
    service = PaymentService(session)
    failed_payment = service.fail_payment(payment_id)
    if not failed_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return failed_payment

@router.patch("/{payment_id}/refund", response_model=PaymentResponse)
def refund_payment(payment_id: int, session: Session = Depends(get_session)):
    service = PaymentService(session)
    refunded_payment = service.refund_payment(payment_id)
    if not refunded_payment:
        raise HTTPException(status_code=404, detail="Payment not found or cannot be refunded")
    return refunded_payment

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, session: Session = Depends(get_session)):
    service = PaymentService(session)
    if not service.delete_payment(payment_id):
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Payment deleted successfully"}