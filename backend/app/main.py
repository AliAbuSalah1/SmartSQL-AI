from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .routers import customers, products, orders, ai_query


app = FastAPI(
    title="SmartSQL AI API",
    version="1.0"
)


# CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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