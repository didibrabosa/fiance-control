from pydantic import BaseModel
from datetime import datetime

class Costs(BaseModel):
    cost_id: int
    account_id: int
    categorie_id: int
    cost_value: float
    due_date: datetime
    created_at: datetime
    updated_at: datetime