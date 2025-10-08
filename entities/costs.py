from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Costs(BaseModel):
    cost_id: Optional[int] = Field(None, description="Cost id") 
    account_id: int = Field(..., description="Account id")
    categorie_id: int = Field(..., description="Categorie id")
    cost_value: float = Field(default=0.00, description="Cost value")
    due_date: Optional[datetime] = Field(default=None, description="Cost due date")
    created_at: datetime = Field(default_factory=datetime.now, description="Cost create date")
    updated_at: Optional[datetime] = Field(default=None, description="Cost update date")