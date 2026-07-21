from sqlalchemy import text
from ..database import engine


def execute_sql(sql):

    try:

        with engine.connect() as connection:

            result = connection.execute(text(sql))

            rows = result.fetchall()

            columns = result.keys()

            data = []

            for row in rows:
                data.append(
                    dict(zip(columns, row))
                )

            return data


    except Exception as e:

        return {
            "error": str(e)
        }