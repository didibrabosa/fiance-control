import logging
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