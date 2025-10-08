import logging
from fastapi import APIRouter
from entities.accounts import Accounts
from services.accounts_service import AccountsService
from repositories.accounts_repository import AccountsRepository
from configs.db_connection import get_db_connection

logger = logging.getLogger(__name__)
service = AccountsService(repository=AccountsRepository(db=get_db_connection()))
router = APIRouter(tags=[Accounts])

@router.post("/accounts")
def create_accounts(account: Accounts):
    logger.debug("Starting to create a account...")
    account_created = service.create_accounts(account)

    logger.debug(f"Created account = {account_created}")
    return account_created

@router.get("/accounts")
def get_all_accounts():
    logger.debug("Starting to get all accounts...")
    return service.get_all_accounts()

@router.put("/accounts/{id}")
def update_accounts(id: int, account: Accounts):
    logger.debug("Starting to updat a account... ")
    account.account_id = id
    account_updated = service.update_accounts(account)

    logger.debug(f"Updated account = {account_updated}")
    return account_updated
