from pathlib import Path

from app.database.db import get_connection


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    schema_path = Path(__file__).parent / "schema.sql"

    with open(schema_path, "r") as f:

        schema = f.read()

    cursor.execute(schema)

    conn.commit()

    cursor.close()

    conn.close()

    print("Database initialized successfully.")
