from fastapi import APIRouter

from ..ai.schema_reader import get_database_schema
from ..ai.sql_generator import generate_sql
from ..ai.sql_executor import execute_sql
from ..ai.local_sql_generator import generate_local_sql


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


    # Try local AI first
    sql = generate_local_sql(question)


    # If no local rule exists, use OpenAI
    if sql is None:

        sql = generate_sql(
            question,
            schema
        )


    if isinstance(sql, dict) and "error" in sql:

        return sql


    result = execute_sql(sql)


    return {
        "question": question,
        "sql": sql,
        "result": result
    }