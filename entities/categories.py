from pydantic import BaseModel

class Categories(BaseModel):
    categorie_id: int
    categorie_name: str