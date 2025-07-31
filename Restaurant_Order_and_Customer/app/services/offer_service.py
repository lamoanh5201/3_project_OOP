from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from app.models.offer_model import Offer
from app.schemas.offer_schema import OfferCreate, OfferUpdate

class OfferService:
    def __init__(self, session: Session):
        self.session = session

    def create_offer(self, offer_data: OfferCreate) -> Offer:
        offer = Offer(**offer_data.dict())
        self.session.add(offer)
        self.session.commit()
        self.session.refresh(offer)
        return offer

    def get_offer(self, offer_id: int) -> Optional[Offer]:
        return self.session.get(Offer, offer_id)

    def get_offers(self, skip: int = 0, limit: int = 100) -> List[Offer]:
        statement = select(Offer).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def get_active_offers(self) -> List[Offer]:
        current_time = datetime.utcnow()
        statement = select(Offer).where(
            Offer.is_active == True,
            Offer.start_date <= current_time,
            Offer.end_date >= current_time
        )
        return self.session.exec(statement).all()

    def update_offer(self, offer_id: int, offer_data: OfferUpdate) -> Optional[Offer]:
        offer = self.session.get(Offer, offer_id)
        if offer:
            for key, value in offer_data.dict(exclude_unset=True).items():
                setattr(offer, key, value)
            self.session.commit()
            self.session.refresh(offer)
        return offer

    def delete_offer(self, offer_id: int) -> bool:
        offer = self.session.get(Offer, offer_id)
        if offer:
            self.session.delete(offer)
            self.session.commit()
            return True
        return False

    def deactivate_offer(self, offer_id: int) -> Optional[Offer]:
        offer = self.session.get(Offer, offer_id)
        if offer:
            offer.is_active = False
            self.session.commit()
            self.session.refresh(offer)
        return offer