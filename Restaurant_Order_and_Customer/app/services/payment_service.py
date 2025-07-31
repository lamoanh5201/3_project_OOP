from sqlmodel import Session, select
from typing import List, Optional
from app.models.payment_model import Payment, PaymentStatus
from app.schemas.payment_schema import PaymentCreate, PaymentUpdate

class PaymentService:
    def __init__(self, session: Session):
        self.session = session

    def create_payment(self, payment_data: PaymentCreate) -> Payment:
        payment = Payment(**payment_data.dict())
        self.session.add(payment)
        self.session.commit()
        self.session.refresh(payment)
        return payment

    def get_payment(self, payment_id: int) -> Optional[Payment]:
        return self.session.get(Payment, payment_id)

    def get_payments(self, skip: int = 0, limit: int = 100) -> List[Payment]:
        statement = select(Payment).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def get_payments_by_order(self, order_id: int) -> List[Payment]:
        statement = select(Payment).where(Payment.order_id == order_id)
        return self.session.exec(statement).all()

    def get_payments_by_status(self, status: PaymentStatus) -> List[Payment]:
        statement = select(Payment).where(Payment.status == status)
        return self.session.exec(statement).all()

    def update_payment(self, payment_id: int, payment_data: PaymentUpdate) -> Optional[Payment]:
        payment = self.session.get(Payment, payment_id)
        if payment:
            for key, value in payment_data.dict(exclude_unset=True).items():
                setattr(payment, key, value)
            self.session.commit()
            self.session.refresh(payment)
        return payment

    def delete_payment(self, payment_id: int) -> bool:
        payment = self.session.get(Payment, payment_id)
        if payment:
            self.session.delete(payment)
            self.session.commit()
            return True
        return False

    def complete_payment(self, payment_id: int, transaction_id: str = None) -> Optional[Payment]:
        payment = self.session.get(Payment, payment_id)
        if payment:
            payment.status = PaymentStatus.COMPLETED
            if transaction_id:
                payment.transaction_id = transaction_id
            self.session.commit()
            self.session.refresh(payment)
        return payment

    def fail_payment(self, payment_id: int) -> Optional[Payment]:
        payment = self.session.get(Payment, payment_id)
        if payment:
            payment.status = PaymentStatus.FAILED
            self.session.commit()
            self.session.refresh(payment)
        return payment

    def refund_payment(self, payment_id: int) -> Optional[Payment]:
        payment = self.session.get(Payment, payment_id)
        if payment and payment.status == PaymentStatus.COMPLETED:
            payment.status = PaymentStatus.REFUNDED
            self.session.commit()
            self.session.refresh(payment)
        return payment