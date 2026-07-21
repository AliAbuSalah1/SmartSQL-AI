# SmartSQL AI

AI-powered Text-to-SQL application that allows users to query databases using natural language.

## Features

- Convert natural language questions into SQL queries
- Execute generated SQL against PostgreSQL database
- Display query results dynamically
- FastAPI backend
- React frontend
- Local SQL generator fallback without API dependency

## Example

User:

show me expensive products

Generated SQL:

SELECT * FROM products WHERE price > 500;

Result:

Laptop | 900


## Tech Stack

Backend:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Python

Frontend:
- React
- Vite
- JavaScript


## Run Backend

```bash
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload