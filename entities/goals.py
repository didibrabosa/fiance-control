from pydantic import BaseModel

class Goals(BaseModel):
    goal_id: int
    account_id: int
    goal_value: float
    current_value: float