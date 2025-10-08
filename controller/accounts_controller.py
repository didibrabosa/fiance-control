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
    logger.debug("Started to creating a account...")
    account_created = service.create_accounts(account)

    logger.debug(f"Created account = {account}")
    return account_created

@router.get("/accounts")
def get_all_accounts():
    logger.debug("Started to getting the accounts...")
    return service.get_all_accounts()
