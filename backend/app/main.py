from fastapi import FastAPI
from .database import engine
from .routers import customers, products, orders
app = FastAPI(
    title="SmartSQL AI API",
    version="1.0"
)


app.include_router(customers.router)
app.include_router(products.router)
app.include_router(orders.router)
@app.get("/")
def home():
    return {
        "message": "SmartSQL AI Backend Running"
    }