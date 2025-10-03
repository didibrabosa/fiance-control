import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT")
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None