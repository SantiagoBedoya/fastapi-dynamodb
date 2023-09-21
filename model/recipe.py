from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(...)
    uom: str = Field(...)
    amount: Decimal = Field(...)

class Recipe(BaseModel):
    uid: Optional[str] = None
    title: str = Field(..., examples=['Recipe title'])
    author: str = Field(..., examples=['Amazing Chef'])
    description: Optional[str] = Field(..., examples=['What makes this recipe special'])
    steps: List[str] = Field(..., examples=[['Step1', 'Step2']])
    ingredients: List[Ingredient]