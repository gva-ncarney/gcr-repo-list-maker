"""
I am an example data model.

I extend the pydantic.BaseModel class
"""
from pydantic import BaseModel
from typing import Optional


class ExampleModel(BaseModel):
    name: Optional[str]
