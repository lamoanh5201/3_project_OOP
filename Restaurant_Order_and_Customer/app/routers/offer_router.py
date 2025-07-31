from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.services.offer_service import OfferService
from app.schemas.offer_schema import OfferCreate, OfferUpdate, OfferResponse

router = APIRouter()

@router.post("/", response_model=OfferResponse)
def create_offer(offer: OfferCreate, session: Session = Depends(get_session)):
    service = OfferService(session)
    return service.create_offer(offer)

@router.get("/{offer_id}", response_model=OfferResponse)
def get_offer(offer_id: int, session: Session = Depends(get_session)):
    service = OfferService(session)
    offer = service.get_offer(offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

@router.get("/", response_model=List[OfferResponse])
def get_offers(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    service = OfferService(session)
    return service.get_offers(skip=skip, limit=limit)

@router.get("/active/list", response_model=List[OfferResponse])
def get_active_offers(session: Session = Depends(get_session)):
    service = OfferService(session)
    return service.get_active_offers()

@router.put("/{offer_id}", response_model=OfferResponse)
def update_offer(offer_id: int, offer: OfferUpdate, session: Session = Depends(get_session)):
    service = OfferService(session)
    updated_offer = service.update_offer(offer_id, offer)
    if not updated_offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return updated_offer

@router.patch("/{offer_id}/deactivate", response_model=OfferResponse)
def deactivate_offer(offer_id: int, session: Session = Depends(get_session)):
    service = OfferService(session)
    deactivated_offer = service.deactivate_offer(offer_id)
    if not deactivated_offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return deactivated_offer

@router.delete("/{offer_id}")
def delete_offer(offer_id: int, session: Session = Depends(get_session)):
    service = OfferService(session)
    if not service.delete_offer(offer_id):
        raise HTTPException(status_code=404, detail="Offer not found")
    return {"message": "Offer deleted successfully"}