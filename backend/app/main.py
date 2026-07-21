from fastapi import FastAPI
from .database import engine
from .routers import customers, products, orders, ai_query
app = FastAPI(
    title="SmartSQL AI API",
    version="1.0"
)


app.include_router(customers.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(ai_query.router)
@app.get("/")
def home():
    return {
        "message": "SmartSQL AI Backend Running"
    }