import os
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection(retries: int = 5, delay: int = 2):
    """Establishes and returns a connection to the PostgreSQL database with retry on failure."""
    for attempt in range(retries):
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
            print(f"Error connecting to the database (attempt {attempt+1}/{retries}): {e}")
            time.sleep(delay)
    return None