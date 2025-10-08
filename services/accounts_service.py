import logging
from datetime import datetime
from typing import List
from entities.accounts import Accounts
from repositories.accounts_repository import AccountsRepository

class AccountsService:
    def __init__(self, repository: AccountsRepository):
        self.logger = logging.getLogger(__name__)
        self.repository = repository

    def create_accounts(self, accounts: Accounts) -> Accounts:
        self.logger.info("Creating account...")
        return self.repository.create_accounts(accounts)
    
    def get_all_accounts(self) -> List[Accounts]:
        self.logger.info("Getting accounts...")
        return self.repository.get_all_accounts()
    
    def get_account_by_id(self, id: int) -> Accounts:
        self.logger.info("Getting account...")
        return self.repository.get_account_by_id(id)
    
    def update_accounts(self, accounts: Accounts) -> Accounts:
        self.logger.info("Updating account...")
        accounts.updated_at = datetime.now()
        return self.repository.update_accounts(accounts)
    
    def delete_accouts(self, id: int) -> Accounts:
        self.logger.info("Deleting account...")
        return self.repository.delete_accounts(id)