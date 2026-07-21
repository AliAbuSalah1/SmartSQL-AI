from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Product


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_products(db: Session = Depends(get_db)):

    products = db.query(Product).all()

    return products