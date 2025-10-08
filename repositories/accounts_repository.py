import logging
from typing import List
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

    def get_all_accounts(self) -> List[Accounts]:
        self.logger.info("Getting every account in database")
        try:
            with self.db.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT account_id, account_name, account_status, balance, debt, created_at, updated_at
                    FROM accounts
                    WHERE account_status = true
                    """)
                rows = cursor.fetchall()
                accounts_list = []

                for row in rows:
                    account = self.map_accounts_row_to_model(row)
                    accounts_list.append(account)
                
                return accounts_list
        except DatabaseError as ex:
            self.logger.error(f"Failed to getting accounts in the database. Error: {ex}")
            self.db.rollback()
            raise

    def get_account_by_id(self, id: int) -> Accounts:
        self.logger.info("Getting a account by id in database")
        try:
            with self.db.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT account_id, account_name, account_status, balance, debt, created_at, updated_at
                    FROM accounts
                    WHERE account_id = %s;
                    """, (id,))
                result = cursor.fetchone()
                return self.map_accounts_row_to_model(result)
        except DatabaseError as ex:
            self.logger.error(f"Failed to getting account in the database. Error: {ex}")
            self.db.rollback()
            raise

    def update_accounts(self, accounts: Accounts) -> Accounts:
        self.logger.info("Updating account in Database")
        try:
            with self.db.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE accounts
                    SET 
                        account_name = %s,
                        account_status = %s,
                        balance = %s,
                        debt = %s,
                        updated_at = %s
                    WHERE account_id = %s
                    RETURNING account_id;
                    """,
                    (
                        accounts.account_name,
                        accounts.account_status,
                        accounts.balance,
                        accounts.debt,
                        accounts.updated_at,
                        accounts.account_id
                    ),
                )
                result = cursor.fetchone()

                if result is None:
                    raise ValueError(f"Account with id {accounts.account_id} not found.")

            self.db.commit()
            return accounts
        except DatabaseError as ex:
            self.logger.error(f"Failed to update account in the database. Error: {ex}")
            self.db.rollback()
            raise

    def map_accounts_row_to_model(self, row: List) -> Accounts:
        return Accounts(
            account_id=row[0],
            account_name=row[1],
            account_status=row[2],
            balance=row[3],
            debt=row[4],
            created_at=row[5],
            updated_at=row[6],
        )