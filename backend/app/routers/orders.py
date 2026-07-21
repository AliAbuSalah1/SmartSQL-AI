from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Order


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_orders(db: Session = Depends(get_db)):

    orders = db.query(Order).all()

    return orders