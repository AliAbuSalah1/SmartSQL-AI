from fastapi import FastAPI
from .database import engine


app = FastAPI(
    title="SmartSQL AI API"
)


@app.get("/")
def home():
    try:
        connection = engine.connect()
        connection.close()

        return {
            "message": "Database connected successfully"
        }

    except Exception as e:
        return {
            "error": str(e)
        }