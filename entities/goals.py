from pydantic import BaseModel, Field
from typing import Optional

class Goals(BaseModel):
    goal_id: Optional[int] = Field(None, description="Goal id")
    account_id: int = Field(..., description="Account id")
    goal_value: float = Field(default=0.00, description="Goal value")
    current_value: float = Field(default=0.00, description="Goal current value")