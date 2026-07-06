import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def get_connection():

    database_url = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(database_url)

    return conn
