from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Customer


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_customers(db: Session = Depends(get_db)):

    customers = db.query(Customer).all()

    return customers