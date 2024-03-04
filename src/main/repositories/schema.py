import pydantic as _pydantic
from typing import List

class _RecipeBase(_pydantic.BaseModel):
    title: str
    ingredients: str
    method: str

class RecipeCreate(_RecipeBase):
    pass

class Recipe(_RecipeBase):
    id: int
    