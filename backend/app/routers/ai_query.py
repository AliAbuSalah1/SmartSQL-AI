from fastapi import APIRouter

from ..ai.schema_reader import get_database_schema
from ..ai.sql_generator import generate_sql


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.get("/schema")
def database_schema():

    return get_database_schema()



@router.post("/ask")
def ask_ai(question: str):

    schema = get_database_schema()

    sql = generate_sql(
        question,
        schema
    )

    return {
        "question": question,
        "sql": sql
    }