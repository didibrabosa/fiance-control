from pydantic import BaseModel
from datetime import datetime

class Accounts(BaseModel):
    account_id: int
    account_name: str
    account_status: bool
    balance: float
    debt: float
    created_at: datetime
    updated_at: datetime