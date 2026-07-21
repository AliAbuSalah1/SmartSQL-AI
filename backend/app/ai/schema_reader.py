from sqlalchemy import inspect
from ..database import engine


def get_database_schema():

    inspector = inspect(engine)

    schema = {}

    for table_name in inspector.get_table_names():

        columns = []

        for column in inspector.get_columns(table_name):
            columns.append(column["name"])

        schema[table_name] = columns

    return schema