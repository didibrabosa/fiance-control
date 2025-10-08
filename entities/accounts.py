from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Accounts(BaseModel):
    account_id: Optional[int] = Field(None, description="Account id")
    account_name: str = Field(..., description="Account name")
    account_status: bool = Field(default=True, description="Account status")
    balance: float = Field(default=0.00, description="Account balance")
    debt: float = Field(default=0.00, description="Account debt")
    created_at: datetime = Field(default_factory=datetime.now, description="Account create date")
    updated_at: Optional[datetime] = Field(default=None, description="Account update date")