import logging
from psycopg2 import DatabaseError
from entities.accounts import Accounts
from configs.db_connection import get_db_connection

class AccountsRepository:
    def __init__(self, db: get_db_connection):
        self.logger = logging.getLogger(__name__)
        self.db = db

    def create_accounts(self, accounts: Accounts) -> Accounts:
        self.logger.info("Inserting a new account in database")
        try:
            with self.db.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO accounts
                     (account_name, account_status, balance, debt, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING account_id;
                    """,
                    (
                        accounts.account_name,
                        accounts.account_status,
                        accounts.balance,
                        accounts.debt,
                        accounts.created_at,
                        accounts.updated_at
                    ), 
                )
                row = cursor.fetchone()
                self.db.commit()
                accounts.account_id = row[0]
                return accounts
        except DatabaseError as ex:
            self.logger.error(f"Failed to insert account in the database. Error: {ex}")
            self.db.rollback()
            raise