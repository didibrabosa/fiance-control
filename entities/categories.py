from pydantic import BaseModel, Field
from typing import Optional

class Categories(BaseModel):
    categorie_id: Optional[int] = Field(None, description="Categorie id")
    categorie_name: str = Field(..., description="Categorie name")